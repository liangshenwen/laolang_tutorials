"""
turtle内置模块:
https://docs.python.org/zh-cn/3/library/html#
"""
import time
import turtle
from turtle import *


def draw_circle():
    """
    画圆的各种方式
    """
    reset()
    print('mode:', mode())
    hideturtle()
    # 圆心在左边30像素，逆时针画圆
    t1 = Turtle()
    print('t1.heading:', t1.heading())
    t1.speed(1)
    t1.penup()
    t1.goto(-100, 100)
    t1.pendown()
    t1.circle(30)
    print('t1.heading:', t1.heading())

    # 圆心在右边30像素，顺时针画圆
    t2 = Turtle()
    print('t2.heading:', t2.heading())
    t2.speed(1)
    t2.penup()
    t2.goto(100, 100)
    t2.pendown()
    t2.circle(-30)
    print('t2.heading:', t2.heading())

    # 圆心在左边30像素，逆时针画半个画圆
    t3 = Turtle()
    print('t3.heading:', t3.heading())
    t3.speed(1)
    t3.penup()
    t3.goto(-100, -100)
    t3.pendown()
    t3.circle(30, 180)
    print('t3.heading:', t3.heading())

    # 圆心在右边30像素，顺时针画半个画圆
    t4 = Turtle()
    print('t4.heading:', t4.heading())
    t4.speed(1)
    t4.penup()
    t4.goto(100, -100)
    t4.pendown()
    t4.circle(-30, 180)
    print('t4.heading:', t4.heading())

    # 圆心在右边30像素，以倒退的方式逆时针画半个画圆
    t5 = Turtle()
    print('t5.heading:', t5.heading())
    t5.speed(1)
    t5.penup()
    t5.goto(100, -200)
    t5.pendown()
    t5.circle(-30, -180)
    print('t5.heading:', t5.heading())

    done()


def tracer_delay_speed():
    """
    tracer(n=None, delay=None)
    参数
      n -- 非负整型数
      delay -- 非负整型数

    启用/禁用海龟动画并设置刷新图形的延迟时间。如果指定 n 值，则只有每第 n 次屏幕刷新会实际执行。(可被用来加速复杂图形的绘制。)
    如果调用时不带参数，则返回当前保存的 n 值。

    delay(delay=None)
    参数
      delay -- 正整型数

    设置或返回以毫秒数表示的延迟值 delay。(这约等于连续两次画布刷新的间隔时间。) 绘图延迟越长，动画速度越慢。

    speed(speed=None)
    参数
      speed -- 一个 0..10 范围内的整型数或速度字符串 (见下)

    设置海龟移动的速度为 0..10 表示的整型数值。如未指定参数则返回当前速度。

    如果输入数值大于 10 或小于 0.5 则速度设为 0。速度字符串与速度值的对应关系如下:

    "fastest": 0 最快

    "fast": 10 快

    "normal": 6 正常

    "slow": 3 慢

    "slowest": 1 最慢

    速度值从 1 到 10，画线和海龟转向的动画效果逐级加快。

    注意: speed = 0 表示 没有 动画效果。forward/back 将使海龟向前/向后跳跃，同样的 left/right 将使海龟立即改变朝向。

    """

    # 默认的速度
    def example1():
        reset()
        print('delay 1:', delay())
        print('tracer 1:', tracer())
        print('speed 1:', speed())
        dist = 4
        for i in range(28):
            fd(dist)
            rt(90)
            dist += 4

    # 通过设置delay值来降低动画速度
    def example2():
        reset()
        tracer(1, 100)
        print('speed 2:', speed())
        print('delay 2:', delay())
        print('tracer 2:', tracer())
        dist = 4
        for i in range(5):
            fd(dist)
            rt(90)
            dist += 4

    # 通过设置speed值来提升动画速度
    def example3():
        reset()
        speed(10)
        print('speed 3:', speed())
        print('delay 3:', delay())
        print('tracer 3:', tracer())
        dist = 4
        for i in range(5):
            fd(dist)
            rt(90)
            dist += 4

    # 通过设置把tracer设置为0来取消画图的动画效果
    def example4():
        reset()
        tracer(0)
        print('speed 4:', speed())
        print('delay 4:', delay())
        print('tracer 4:', tracer())
        dist = 2
        for i in range(200):
            fd(dist)
            rt(90)
            dist += 2

    # 每隔2次画图刷新一次屏幕，这样可以提高画图的时间
    def example5():
        reset()
        tracer(8, 100)
        print('speed 5:', speed())
        print('delay 5:', delay())
        print('tracer 5:', tracer())
        time.sleep(1)
        dist = 2
        for i in range(200):
            fd(dist)
            rt(90)
            dist += 2

    def example6():
        reset()
        # loop for motion with
        # default tracer as 1
        for i in range(20):
            forward(1 + 1 * i)
            right(45)

        time.sleep(5)
        # set tracer values as (2,0)
        # 2 -> for screen update
        # 0 -> delay
        tracer(n=2, delay=0)

        # loop for motion with
        # above tracer values
        for i in range(20, 40):
            forward(1 + 1 * i)
            right(45)

        time.sleep(5)
        # set tracer values as (1,50)
        # 1 -> for screen update
        # 50 -> delay
        tracer(n=1, delay=50)

        # loop for motion with
        # above tracer values
        for i in range(40, 60):
            forward(1 + 1 * i)
            right(45)

    # example1()
    # example5()
    example6()

    done()


if __name__ == '__main__':
    # draw_circle()
    tracer_delay_speed()
