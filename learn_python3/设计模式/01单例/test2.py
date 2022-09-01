from tkinter import *

root = Tk()

la1 = Label(root, text='用户名：')
la1.grid(row=0, column=0)  # 0行0列

en1 = Entry(root)  # 用户名文本框
en1.grid(row=0, column=1, columnspan=2)  # 0行1列，跨2列

la2 = Label(root, text='密　码：')
la2.grid(row=1, column=0)

en2 = Entry(root)  # 密码文本框
en2.grid(row=1, column=1, columnspan=2)  # 1行1列，跨2列

but1 = Button(root, text="确定")
but1.grid(row=2, column=1)
but2 = Button(root, text="取消")
but2.grid(row=2, column=2)

root.mainloop()