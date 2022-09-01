import tkinter as tk
root= tk.Tk()
root.title('锚点问题')
root.geometry('500x500')    # 设置窗口为500x500
canvas = tk.Canvas(root, width=400, height=400, bg='yellow')   # 创建400x400，背景为黄色的画布
image_file = tk.PhotoImage(file='个人头像.png')  # 创建图片对象
image = canvas.create_image(200, 200,  anchor='center', image=image_file)     # 将图片放置在画布上
canvas.pack()         # 放置画布
root.mainloop()