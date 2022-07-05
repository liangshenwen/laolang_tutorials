import turtle
turtle.title('五角星')
deg = 36 # 角角度
n = 100 # 边长
turtle.speed(1)
turtle.pencolor('#069')
turtle.begin_fill()
turtle.fillcolor('#069')
turtle.left(deg)
for _ in range(5):
    turtle.forward(n)
    turtle.left(180 - deg)
turtle.end_fill()

turtle.hideturtle()
turtle.done()