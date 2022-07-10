from turtle import *

setup(1500, 1400, 0, 0)
title('小蟒蛇')
speed(1)
pensize(30)  # 画笔尺寸
pencolor("green")
seth(-40)  # 前进的方向
rad = 70  # 身体弯曲半径
angle = 80  # 身体弯曲的角长度
neck_rad = 15
length = 2  # 身体部分有4段弯曲
for _ in range(length):
    circle(rad, angle)
    circle(-rad, angle)

circle(rad, angle / 2)
forward(rad / 2)  # 直线前进
circle(neck_rad, 180)
forward(rad / 4)

done()
