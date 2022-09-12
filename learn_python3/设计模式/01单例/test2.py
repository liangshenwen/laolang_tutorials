import tkinter as tk

window = tk.Tk()
# 设置窗口大小
winWidth = 600
winHeight = 400
# 获取屏幕分辨率
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()

x = int((screenWidth - winWidth) / 2)
y = int((screenHeight - winHeight) / 2)

# 设置主窗口标题
window.title("绑定事件参数说明")
# 设置窗口初始位置在屏幕居中
window.geometry("%sx%s+%s+%s" % (winWidth, winHeight, x, y))
# 设置窗口宽高固定
window.resizable(0, 0)


def callBack(event):
    print("button is click")


btn = tk.Button(window, text="点击")
btn.bind("<Button-1>", callBack)
btn.pack()


def windowBack(event):
    print(event.char)


window.bind("<Key>", windowBack)

window.mainloop()
