import turtle

turtle.title('长方形')
turtle.begin_fill()
turtle.fillcolor('#069')
for x in range(1, 5):
    if x % 2 == 1:
        n = 100
    else:
        n = 50
    turtle.forward(n)
    turtle.right(90)
turtle.end_fill()
turtle.hideturtle()
turtle.done()