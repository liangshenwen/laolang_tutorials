import turtle

turtle.title('围棋棋盘')
g = 25 # 格子的大小
num_x = 18 # 横线的条数
num_y = 18 # 竖线的条数
r = 5 # 棋盘圆点的半径
j = 3  # 棋盘圆点之间相隔的格子数量


turtle.speed(15)
# 绘制横线
ruler_y = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十', '十一',  '十二', '十三', '十四', '十五', '十六', '十七', '十八', '十九']
for i in range(num_x + 1):
    if (i == 0) or (i == num_x):
        turtle.pensize(3)
    else:
        turtle.pensize(1)
    #  画线
    turtle.up()
    turtle.goto(-num_x / 2 * g, num_y / 2 * g - g * i)
    turtle.down()
    turtle.forward(num_y * g)
    # 写字
    turtle.up()
    turtle.goto(-num_x / 2 * g - g, num_y / 2 * g - g * i - g / 3)
    #turtle.write(ruler_y[x], align="center", font=("Courier", 10, "bold"))
    turtle.write(str(i + 1) if i > 9 else '0' + str(i), align="center", font=("Courier", 10, "bold"))
    turtle.down()

# 绘制竖线
turtle.right(90)
for i in range(num_y + 1):
    if (i == 0) or (i == num_y):
        turtle.pensize(3)
    else:
        turtle.pensize(1)
    # 画竖线
    turtle.up()
    turtle.goto(-num_x / 2 * g + g * i, num_y / 2 * g)
    turtle.down()
    turtle.forward(num_x * g)

    # 写字
    turtle.up()
    turtle.goto(-num_x / 2 * g + g * i, num_y / 2 * g + g / 2)
    turtle.write(str(i + 1) if i > 9 else '0' + str(i), align="center", font=("Courier", 10, "bold"))
    turtle.down()

#  绘画9个棋盘圆点
turtle.pensize(1)
for y in range(3):
    for x in range(3):
        turtle.up()
        turtle.begin_fill()
        turtle.fillcolor('black')
        turtle.goto(-num_x / 2 * g + (j * g) * (2 * x + 1) - r, num_y / 2 * g - (j * g) * (2 * y + 1))
        turtle.down()
        turtle.circle(r)
        turtle.end_fill()

turtle.hideturtle()
turtle.done()