import turtle
turtle.title('网格球')
turtle.setup(500, 500)

turtle.pencolor("green")
turtle.pensize(4)
turtle.speed(0)
turtle.seth(90)

# 画球体
n = 1
while n <= 36:
    turtle.circle(100)
    turtle.left(10)
    n += 1

turtle.getcanvas().postscript(file='网格球_1.eps')
turtle.mainloop()
