from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from sys import argv, stderr, exit
from re import match
from threading import Thread

IPP = r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"
PORT_START = 8000
PORT_END = 9000
PORT_RANGE = range(PORT_START, PORT_END + 1)
BUFFER_SIZE = 1024
host = None
port = None
clients = {}

def start_receiver(nick: str, cSock: socket):
    
    try:
        while True:
            data = cSock.recv(BUFFER_SIZE)            
            if not data:
                raise Exception(f"{nick}님과의 연결이 종료되었습니다.")
            for nick, client in clients.items():
                client['sock'].send(data)
    except Exception as e:
        print(e)
    finally:            
        if nick in clients: 
            del clients[nick]
    
def open_server(host: str, port: int):
    try:        
        sSock = socket(AF_INET, SOCK_STREAM)
        print("서버 소켓을 생성하였습니다.")
        sSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)                
        print("소켓 옵션을 지정하였습니다.")
        sSock.bind((host, port))
        print(f"소켓을 {host}의 {port} 포트에 바인딩하였습니다.")
        sSock.listen()        
        print("소켓 경청모드로 전환하였습니다.")
        while True:            
            try:
                (cSock, cInfo) = sSock.accept()
                print(f"{cInfo[0]} 클라이언트가 접속하였습니다.")
                nick = cSock.recv(BUFFER_SIZE).decode()
                print(f"{cInfo[0]} 클라이언트의 닉네임이 {nick}으로 설정되었습니다.")
                cSock.send("OK".encode())
                print(f"{cInfo[0]} 클라이언트에 \"OK\"를 송신하였습니다.")
                clients[nick] = {'info': cInfo, 'sock': cSock}                
                ct = Thread(target=start_receiver, args=(nick, cSock))
                ct.daemon = True
                ct.start()
            except Exception as e:
                print(e)
    except Exception as e:
        pass
    finally:
        if sSock:
            sSock.close()

if __name__ == '__main__':
    if len(argv) < 3:
        print("올바르지 않은 명령행입니다.", file=stderr)
        print(f"사용법 : {argv[0]} 바인딩주소 바인딩포트")
        exit(1)
        
    try:
        host = argv[1]
        if not match(IPP, host):
            raise Exception("올바르지 않은 호스트 주소입니다.")
        
        port = int(argv[2])
        if not port in PORT_RANGE:
            raise Exception(f"{PORT_START}번부터 {PORT_END}번 사이의 포트를 지정해야 합니다.")
        
        open_server(host, port)
                
    except ValueError as e:
        print('올바르지 않은 포트번호입니다.', file=stderr)
        exit(1)
    except Exception as e:
        print(e, file=stderr)
        exit(1)
    finally:
        print("프로그램을 종료합니다.")