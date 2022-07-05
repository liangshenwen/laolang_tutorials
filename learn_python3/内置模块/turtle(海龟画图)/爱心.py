from turtle import *

speed(1)
color('red', 'pink')  # 画笔色red，背景色pink
begin_fill()
left(135)  # 左转135°
fd(100)  # 前进100像素
right(180)  # 画笔掉头

circle(30, -180)

backward(35)  # 由于此时画笔方向约为绝对方向的135°，需倒退画线
right(90)
forward(35)
circle(-30, 180)
fd(100)
end_fill()
hideturtle()
done()