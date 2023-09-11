import tkinter
import tkinter.messagebox
import tkinter.ttk
import re
import threading
from socket import socket, AF_INET, SOCK_STREAM

IPP = r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"
BUFFER_SIZE = 1024


class MainWin:
    def __init__(self):
        self.__sock = None
        self.__receiver = None
        self.__host = None
        self.__port = None
        self.__nick = None
        self.__root = tkinter.Tk()
        self.__root.geometry('600x350')
        self.__root.title('채팅프로그램 Ver 1.0')

        menubar = tkinter.Menu(self.__root)
        self.__connectMenu = tkinter.Menu(menubar, tearoff=False)
        self.__connectMenu.add_command(label='서버접속', command=self.open_logwin)
        self.__connectMenu.add_command(
            label='연결종료', command=self.disconnect, state='disable')
        self.__connectMenu.add_separator()
        self.__connectMenu.add_command(label='종료', command=self.exit_app)
        menubar.add_cascade(label='연결', menu=self.__connectMenu)
        self.__root.config(menu=menubar)

        mainFrame = tkinter.Frame(self.__root)
        mainFrame.pack(side='top', fill='x', padx=5)

        frameMessage = tkinter.Frame(mainFrame)
        frameMessage.pack(expand=True, fill='both')
        self.__recvMessageBox = tkinter.Text(frameMessage, state='disabled')
        self.__recvMessageBox.pack(expand=True, fill='both')

        frameAction = tkinter.Frame(mainFrame)
        frameAction.pack(expand=True, fill='x', pady=(5, 0))
        self.__sendMessage = tkinter.Entry(
            frameAction, width=50, state='disabled')
        self.__sendMessage.pack(expand=True, side='left', fill='both')
        self.__btnSend = tkinter.Button(
            frameAction, text='전송', width=10, state='disabled', command=self.send_message)
        self.__btnSend.pack(expand=True, side='right', fill='both')

        self.__root.mainloop()

    @property
    def sock(self):
        return self.__sock

    @property
    def nick(self):
        return self.__nick

    def send_message(self):
        message = self.__sendMessage.get()
        if message:
            message = f"{self.__nick} : {message}"
            self.__sock.send(message.encode())
            self.__sendMessage.delete(0, tkinter.END)

    def add_message(self, message):
        self.__recvMessageBox.insert(tkinter.END, message + '\n')

    def open_logwin(self):

        def connect():
            try:
                host = entryHost.get()
                port = entryPort.get()
                nick = entryNick.get()

                if not host:
                    raise Exception("서버주소가 입력되지 않았습니다.")
                if not re.match(IPP, host):
                    raise Exception("올바르지 않은 서버 주소입니다.")
                if not port:
                    raise Exception("포트번호가 입력되지 않았습니다.")
                try:
                    port = int(port)
                except:
                    raise Exception("올바르지 않은 포트번호 입니다.")
                if not nick:
                    raise Exception("닉네임이 입력되지 않았습니다.")

                cSock = socket(AF_INET, SOCK_STREAM)
                cSock.connect((host, port))
                cSock.send(nick.encode())
                data = cSock.recv(BUFFER_SIZE)
                if not data:
                    raise Exception("서버와의 데이터송수신이 실패하였습니다.")
                self.__host = host
                self.__port = port
                self.__nick = nick
                self.__sock = cSock
                self.__receiver = Reciever(self)
                self.__receiver.daemon = True
                self.__receiver.start()
                self.enable()
                toplevel.destroy()
                toplevel.update()

            except Exception as e:
                print(e)

        toplevel = tkinter.Toplevel(self.__root)
        toplevel.title('서버접속')
        toplevel.geometry('250x140')

        mainFrame = tkinter.LabelFrame(toplevel, text='접속정보')
        mainFrame.pack(fill='x', padx=5, pady=5)

        frameHost = tkinter.Frame(mainFrame)
        frameHost.pack(fill='x', padx=(0, 5), pady=2)
        labelHost = tkinter.Label(
            frameHost, text='서버주소', width=8, justify='center')
        labelHost.pack(side='left')
        entryHost = tkinter.Entry(frameHost)
        entryHost.pack(side='right', fill='x')

        framePort = tkinter.Frame(mainFrame)
        framePort.pack(fill='x', padx=(0, 5), pady=2)
        labelPort = tkinter.Label(
            framePort, text='포트번호', width=8, justify='center')
        labelPort.pack(side='left')
        entryPort = tkinter.Entry(framePort)
        entryPort.pack(side='right', fill='x')

        frameNick = tkinter.Frame(mainFrame)
        frameNick.pack(fill='x', padx=(0, 5), pady=2)
        labelNick = tkinter.Label(
            frameNick, text='닉네임', width=8, justify='center')
        labelNick.pack(side='left')
        entryNick = tkinter.Entry(frameNick)
        entryNick.pack(side='right', fill='x')

        frameAction = tkinter.Frame(mainFrame)
        frameAction.pack(fill='x', padx=5, pady=(2, 5))
        btnConnect = tkinter.Button(frameAction, text='접속하기', command=connect)
        btnConnect.pack(side='left', expand=True, fill='x')
        btnCancel = tkinter.Button(
            frameAction, text='취소하기', command=self.disconnect)
        btnCancel.pack(side='right', expand=True, fill='x')

    def disconnect(self):
        try:
            self.__sock.close()
            self.__host = None
            self.__port = None
            self.__nick = None
        except:
            pass
        finally:
            self.__recvMessageBox.delete(1.0, tkinter.END)
            self.__sendMessage.delete(0, tkinter.END)
            self.__sendMessage.config(state='disabled')
            self.__btnSend.config(state='disabled')
            self.__connectMenu.entryconfig(index=0, state='normal')
            self.__connectMenu.entryconfig(index=1, state='disabled')

    def enable(self):
        self.__recvMessageBox.config(state='normal')
        self.__sendMessage.config(state='normal')
        self.__btnSend.config(state='normal')
        self.__connectMenu.entryconfig(index=0, state='disabled')
        self.__connectMenu.entryconfig(index=1, state='normal')

    def exit_app(self):
        if tkinter.messagebox.askokcancel('프로그램종료', '프로그램을 종료하시겠습니까?') == True:
            if self.__sock:
                self.__sock.close()
            self.__root.destroy()


class Reciever(threading.Thread):
    def __init__(self, master):
        super().__init__()
        self.__master = master

    def run(self):
        if self.__master.sock:
            while True:
                try:
                    message = self.__master.sock.recv(BUFFER_SIZE).decode()
                    self.__master.add_message(message)
                except Exception as e:
                    print(e)
                    break
        else:
            self.__master.sock = None
            self.__master.disconnect()


if __name__ == '__main__':
    MainWin()
