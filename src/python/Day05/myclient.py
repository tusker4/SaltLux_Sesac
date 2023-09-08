import sys
import socket

PORT = 9000
BUFFERSIZE = 1024
cSock = None


if len(sys.argv) < 2:
    print("잘못된 명령행입니다")
    print(f"사용법> {sys.argv[0]} 서버주소, file=sys.stderr")
    sys.exit(1)

try:
    cSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cSock.connect((sys.argv[1], PORT))
    while True:
        msg = input("메세지 : ")
        if msg.upper() == 'QUIT':
            break
        cSock.send(msg.encode())
        data = cSock.recv(BUFFERSIZE)
        if not data:
            raise Exception("클라이언트가 연결을 종료하였습니다.")
        print(f"수신 << {data.decode()}")

except Exception as e:
    print(e)
finally:
    if cSock:
        cSock.close()
print('클라이언트를 종료합니다.')
