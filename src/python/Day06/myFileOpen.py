import tkinter
import tkinter.messagebox
import tkinter.filedialog


class MyFileOpen:
    def __init__(self, title="No Name") -> None:
        self.__root = tkinter.Tk()
        self.__root.title(title)
        self.__root.geometry('300x400')
        self.__root.resizable(True, False)
        self.__root.config(padx=5, pady=5)
        self.__initdir__ = '.'
        self.__filetpyes = (('모든파일', '*.*'), ('텍스트파일', '*.txt'))

        self.initWidget()
        self.__root.mainloop()

    def handle_mouse_button1(self, event):
        print(event)

    def initWidget(self):
        self.__content = tkinter.Text(self.__root)
        self.__content.pack(expand=True, fill=tkinter.BOTH)
        self.__content.bind('<Button-1>', self.handle_mouse_button1)

        frmAction = tkinter.Frame(self.__root)
        frmAction.pack(pady=5)

        self.__btnOpen = tkinter.Button(
            frmAction, text='열기', command=self.open_file)
        self.__btnSave = tkinter.Button(
            frmAction, text='저장', command=self.save_file)
        self.__btnExit = tkinter.Button(
            frmAction, text='종료', command=self.quit)

        btnOpen.grid(row=0, column=0, padx=5, sticky='ew')
        btnSave.grid(row=0, column=1, padx=5, sticky='ew')
        btnExit.grid(row=0, column=2, padx=5, sticky='ew')

        frmAction.columnconfigure(0, weight=1)
        frmAction.columnconfigure(1, weight=1)
        frmAction.columnconfigure(2, weight=1)

    def open_file(self):
        filetypes = (('모든파일', '*.*'), ('텍스트파일', '*.txt'))
        tkinter.filedialog.askopenfilename(
            title='파일열기', initialdir='.', filetypes=filetypes)
        with open(filepath, 'r', encoding='utf-8') as fp:
            for line in fp:
                self.__content.insert(tkinter.END, line)

        print('파일오픈')
        print(file)

    def save_file(self):
        savefile = tkinter.filedialog.asksaveasfilename(
            title='파일저장', initialdir=self.__initdir__, filetypes=filetypes)
        filetypes = (())
        print('파일저장')

    def quit(self):
        if tkinter.messagebox.askyesno('프로그램종료', '종료하시겠습니까'):
            self.__root.destroy()


if __name__ == '__main__':
    MyFileOpen("파일열기")
