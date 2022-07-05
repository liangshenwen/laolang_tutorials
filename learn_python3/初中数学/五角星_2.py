import turtle
 
turtle.color('red')  # 画笔颜色和填充颜色都设为红色
turtle.hideturtle()  # 隐藏小海龟
 
turtle.begin_fill()  #开始填充
for i in range(5):
    turtle.forward(100) # 向前走100像素
    turtle.right(144)  # 右转144度

turtle.end_fill()    # 结束填充
turtle.done()