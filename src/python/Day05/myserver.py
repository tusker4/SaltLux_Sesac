import socket
import threading


HOST = '127.0.0.1'
PORT = 9000
sSock = None
BUFFERSIZE = 1024

clients = {}


def receiver(cSock, cinfo):
    while True:
        try:
            data = cSock.recv(BUFFERSIZE)
            if not data:
                raise Exception("클라이언트가 연결을 종료하였습니다.")
            decoded_data = f"{cinfo[0]} : {data.decode()}"
            # 문자열을 그냥보내면 안되고 바이트배열로 보내야한다. -> decode
            for info, sock in clients.items():
                sock.send(decoded_data.encode())
            print(f"송신 >> {decoded_data}")
        except:
            print("서버와의 연결이 종료되었습니다.")  # 송수신의 문제가 생길때 연결종료대신 예외처리
            break
    del clients[cinfo]


try:
    sSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("서버 소켓을 생성하였습니다.")
    sSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print(f"소켓옵션을 지정하였습니다.")
    sSock.bind((HOST, PORT))
    print(f"소켓을 {PORT}번 포트에 바인딩하였습니다.")
    sSock.listen()
    print("소켓을 경청모드로 전환합니다.")
    while True:
        (cSock, cinfo) = sSock.accept()
        print(f"{cinfo[0]} 클라이언트가 접속하였습니다.")
        clients[cinfo] = cSock
        threading.Thread(target=receiver, args=(cSock, cinfo)).start()

        while True:
            try:
                data = cSock.recv()
                # 문자열을 그냥보내면 안되고 바이트배열로 보내야한다. -> decode
                print(f"수신 >> {data.decode()}")
                cSock.send(data)
                print(f"송신 >> {data}")
            except:
                print("서버와의 연결이 종료되었습니다.")  # 송수신의 문제가 생길때 연결종료대신 예외처리
                break
except:
    if sSock:
        sSock.close()  # 연결이 되어있는 상태가 아니니까 닫아야한다.

print("서버프로그램이 종료되었습니다.")
