from turtle import *

speed(1)
color('red', 'pink')  # 画笔色red，背景色pink
begin_fill()
left(135)  # 左转135°
print('left(135):', heading())
forward(100)  # 前进100像素
circle(-30, 180)  # 圆心在海龟右侧30个像素，顺时针画一个半圆
print('circle 1:', heading())
forward(35)  #
left(90)
print('left(90):', heading())
forward(35)
circle(-30, 180)  # 圆心在海龟右侧30个像素，顺时针画一个半圆
print('circle 2:', heading())
forward(100)
end_fill()
hideturtle()
done()
