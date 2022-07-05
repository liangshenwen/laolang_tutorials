import turtle
turtle.title('奥运五环')
x = -120 # x坐标的开始位置
y = 50 # y坐标的开始位置
r = 50 # 圆圈的直径
pensize = 5 # 圆圈的边的大小

turtle.speed(5)  # 画笔移动的速度
# 第一个圈，蓝色
turtle.up()
turtle.goto(x, y)
turtle.down()
turtle.pensize(pensize)
turtle.pencolor('blue')
turtle.circle(r)

# 第二个圈，黑色
turtle.up()
turtle.goto(x + 2.5 * r, y)
turtle.down()
turtle.pensize(pensize)
turtle.pencolor('black')
turtle.circle(r)

# 第三个圈，红色
turtle.up()
turtle.goto(x + (2.5 * r) * 2, y)
turtle.down()
turtle.pensize(pensize)
turtle.pencolor('red')
turtle.circle(r)

# 第四个圈，黄色
turtle.up()
turtle.goto(x + (2.5 * r) * 0.5, y -  r)
turtle.down()
turtle.pensize(pensize)
turtle.pencolor('yellow')
turtle.circle(r)

# 第五个圈，绿色
turtle.up()
turtle.goto(x + (2.5 * r)*1.5, y - r)
turtle.down()
turtle.pensize(5)
turtle.pencolor('green')
turtle.circle(r)

turtle.hideturtle()
turtle.done()