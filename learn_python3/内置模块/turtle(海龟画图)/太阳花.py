from turtle import *
color('red', 'yellow')
speed(5)
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1: # 当画笔再次回到圆点附近的时候
        break
end_fill()
done()