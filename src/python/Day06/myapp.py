import tkinter

# 1. 윈도우 만듬
root = tkinter.Tk()
root.geometry('400x300')
# 윈도우타이틀
root.title('tkinter 윈도우')

# 1-1. pack manager , grid 와 pack 위주로 사용

btn1 = tkinter.Button(root, text='1번째 버튼')
btn2 = tkinter.Button(root, text='2번째 버튼')
btn3 = tkinter.Button(root, text='3번째 버튼')

btn1.place(x=10, y=10, width=100, height=20)  # 호출
btn2.place(x=10, y=10, width=100, height=20)
btn3.place(x=10, y=10, width=100, height=20)
frmMain = tkinter.Frame(root, relief='solid', borderwidth=1)
frmAction = tkinter.LabelFrame(frmMain, text="라벨프라임")
IDIDi = tkinter.Label(frmAction, text='아디')
frmMain.pack(expand=True)
frmAction.pack(expand=True,side='bottom', fill='x', padx=5, pady =5)
IDIDi.pack(side='left')

# 1-2. Frame


root.mainloop()
print('어플리케이션을 종료합니다.')
