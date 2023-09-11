import tkinter


class MyChatClient:

    def __init__(self, title) -> None:
        self.__root = tkinter.Tk()
        self.__root.title(title)
        self.__root.geometry('300x500')
        self.__root.resizable(False, False)
        self.__initMenubar()
        self.__initWidget()
        self.__root.mainloop()

    def initWidget(self):
        menubar = tkinter.Menu(self.__root)
        filemenu = tkinter.Menu(menubar)  # tearoff - 잡아끌어서 분리되게 할수있게?
        filemenu.add_command(label='열기', command=None, )
        filemenu.add_command(label='열기', command=None, state='disabled')
        filemenu.add_separator()
        filemenu.add_command(label='종료', command=None)
        menubar.add_cascade(label='파일', menu=filemenu)
        self.__root.config(menu=filemenu)

    def __initWidget(self):
        frmMain = tkinter.Frame(self.__root)
        ysrcoller = tkinter.Scrollbar(frmMain, orient=tkinter.VERTICAL)
        xsrcoller = tkinter.Scrollbar(frmMain, orient=tkinter.HORIZONTAL)
        self.__txtMain = tkinter.Text(frmMain)
        self.__txtMain.pack = tkinter.Text(expand=True, fill=tkinter.BOTH)
        frmMain.pack(expand=True, fill=tkinter.BOTH)

        frmAction = tkinter.Frame()
        entMessage = tkinter.Entry(frmAction)
        btnSend = tkinter.Button(frmAction, text="전송")
        entMessage.pack(expand=True, fill=tkinter.BOTH)
        

        pass


if __name__ == '__main__':
    MyChatClient("")
