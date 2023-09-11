import tkinter
import tkinter.messagebox
import tkinter.filedialog

class MyFileOpen:
    
    def __init__(self, title='No Name'):
        self.__root = tkinter.Tk()
        self.__root.title(title)
        self.__root.geometry('300x400')
        self.__root.resizable(True, False)
        self.__root.config(padx=5, pady=5)
        self.__initdir = '.'
        self.__filetypes = (('모든파일', '*.*'), ('텍스트 파일', '*.txt'))
        self.initWidget()
        self.__root.mainloop()
        
    def initWidget(self):
        frmContent = tkinter.Frame(self.__root)
        frmContent.pack(expand=True, fill=tkinter.BOTH)
        yscrollbar = tkinter.Scrollbar(frmContent, orient=tkinter.VERTICAL)
        xscrollbar = tkinter.Scrollbar(frmContent, orient=tkinter.HORIZONTAL)
        yscrollbar.pack(side='right', fill=tkinter.Y)
        xscrollbar.pack(side='bottom', fill=tkinter.X)
        
        self.__content = tkinter.Text(frmContent)
        self.__content.config(xscrollcommand=xscrollbar.set)
        self.__content.config(yscrollcommand=yscrollbar.set)
        self.__content.pack(expand=True, fill=tkinter.BOTH)
        
        yscrollbar.config(command=self.__content.yview)
        xscrollbar.config(command=self.__content.xview)
        
        frmAction = tkinter.Frame(self.__root)
        frmAction.pack(expand=True, side=tkinter.BOTTOM, fill=tkinter.X)
        
        self.__btnOpen = tkinter.Button(frmAction, text='열기', command=self.open_file)
        self.__btnSave = tkinter.Button(frmAction, text='저장', command=self.save_file)
        self.__btnExit = tkinter.Button(frmAction, text='종료', command=self.quit)
        self.__btnSave.config(state=tkinter.DISABLED)

        self.__btnOpen.grid(row=0, column=0)
        self.__btnSave.grid(row=0, column=1)
        self.__btnExit.grid(row=0, column=3)
    
    def open_file(self):
        try:
            filepath = tkinter.filedialog.askopenfilename(title='파일열기', initialdir=self.__initdir, filetypes=self.__filetypes)
            with open(filepath, 'r', encoding='utf-8') as fp:
                for line in fp:
                    self.__content.insert(tkinter.END, line)
        except Exception as e:
            print(e)
        else:
            self.__btnSave.config(state='normal')
                
    def save_file(self):
        try:
            savefile = tkinter.filedialog.asksaveasfilename(title='파일저장', initialdir=self.__initdir, filetypes=self.__filetypes)
            with open(savefile, 'w', encoding='utf-8') as fp:
                fp.write(self.__content.get(1.0, tkinter.END))
        except Exception as e:
            print(e)
    
    def quit(self):
        if tkinter.messagebox.askyesnocancel('프로그램 종료', '프로그램을 종료하시겠습니까?') == True:
            self.__root.destroy()
            self.__root.update()
    
if __name__ == '__main__':
    MyFileOpen("파일열기")