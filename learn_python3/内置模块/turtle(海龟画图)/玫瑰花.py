from turtle import *

title('玫瑰花')
# 设置画笔的移动速度
speed(1)

# 设置初始位置
penup()
left(90)
fd(200)
pendown()
right(90)

# 花蕊
fillcolor("red")
begin_fill()
circle(10, 180)
circle(25, 110)
left(50)
circle(60, 45)
circle(20, 170)
right(24)
fd(30)
left(10)
circle(30, 110)
fd(20)
left(40)
circle(90, 70)
circle(30, 150)
right(30)
fd(15)
circle(80, 90)
left(15)
fd(45)
right(165)
fd(20)
left(155)
circle(150, 80)
left(50)
circle(150, 90)
end_fill()

# 花瓣1
left(150)
circle(-90, 70)
left(20)
circle(75, 105)
setheading(60)
circle(80, 98)
circle(-90, 40)

# 花瓣2
left(180)
circle(90, 40)
circle(-80, 98)
setheading(-83)

# 叶子1
fd(30)
left(90)
fd(25)
left(45)
fillcolor("green")
begin_fill()
circle(-80, 90)
right(90)
circle(-80, 90)
end_fill()

right(135)
fd(60)
left(180)
fd(85)
left(90)
fd(80)

# 叶子2
right(90)
right(45)
fillcolor("green")
begin_fill()
circle(80, 90)
left(90)
circle(80, 90)
end_fill()

left(135)
fd(60)
left(180)
fd(60)
right(90)
circle(200, 60)

hideturtle()

done()
