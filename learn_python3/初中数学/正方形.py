import turtle
turtle.title('正方形')
turtle.begin_fill()
turtle.fillcolor('#069')
for x in range(4):
    turtle.forward(100)
    turtle.right(90)
turtle.end_fill()
turtle.hideturtle()

turtle.done()