# 导入turtle画笔并将画笔命名为pen
import turtle as pen
import time

# 设置画笔速度为0(1~10逐渐增加,0最快)
pen.speed(0)
# 只设置画笔颜色为浅蓝色
pen.pencolor('deepskyblue')
# 设置画布的背景颜色
pen.bgcolor('black')
pen.title('螺旋动图')


# 定义函数,用于形成螺旋图
def luo(v):
    # 不断改变螺旋图的初始角度
    pen.seth(v)
    # 抬起画笔
    pen.up()
    # 将画笔置于原点
    pen.goto(0, 0)
    # 放下画笔
    pen.down()
    # 清除上次图形
    pen.clear()
    # 开始绘制螺旋图形
    for j in range(800):
        # 每次画笔前进为原来的3倍
        pen.forward(j * 3)
        # 每次偏转一定角度,使其无法形成闭合的三角形
        pen.right(120 + 1)


# 设置螺旋图的初始位置
n = 0
# 循环绘制
while True:
    # 将tracer置为False,隐藏画笔路经
    pen.tracer(False)
    # 将不断改变螺旋图的角度,使其动起来
    luo(n % 360)
    # 停0.017秒,防止旋转太快导致晕厥
    time.sleep(0.017)
    # 将tracer置为False,显示画笔路经
    # 即:将绘制的图形瞬间显示出来
    pen.tracer(True)
    # 将初始角度加1
    n += 1