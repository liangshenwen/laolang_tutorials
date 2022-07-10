import turtle as t
import time

# 皮卡丘
# 基础设置
t.screensize(800, 600)
t.pensize(2)  # 设置画笔的大小
# t.speed(10)  # 设置画笔速度为10


# 画左偏曲线函数
def radian_left(ang, dis, step, n):
    for i in range(n):
        dis += step  # dis增大step
        t.lt(ang)  # 向左转ang度
        t.fd(dis)  # 向前走dis的步长


def radian_right(ang, dis, step, n):
    for i in range(n):
        dis += step
        t.rt(ang)  # 向左转ang度
        t.fd(dis)  # 向前走dis的步长


# 画耳朵
def init_ears():
    t.color("black", "yellow")
    # 左耳朵曲线
    t.pu()  # 提笔
    t.goto(-50, 100)  # 笔头初始位置
    t.pd()  # 下笔
    t.setheading(110)  # 画笔角度
    t.begin_fill()
    radian_left(1.2, 0.4, 0.1, 40)
    t.setheading(270)  # 画笔角度
    radian_left(1.2, 0.4, 0.1, 40)
    t.setheading(44)  # 画笔角度
    t.forward(32)
    t.end_fill()
    # 右耳朵曲线
    t.pu()  # 提笔
    t.goto(50, 100)  # 笔头初始位置
    t.pd()  # 下笔
    t.setheading(70)  # 画笔角度
    t.begin_fill()
    radian_right(1.2, 0.4, 0.1, 40)
    t.setheading(270)  # 画笔角度
    radian_right(1.2, 0.4, 0.1, 40)
    t.setheading(136)  # 画笔角度
    t.forward(32)
    t.end_fill()
    # 耳朵黑
    t.begin_fill()
    t.fillcolor("black")
    t.pu()  # 提笔
    t.goto(88, 141)  # 笔头初始位置
    t.pd()  # 下笔
    t.setheading(35)  # 画笔角度
    radian_right(1.2, 1.6, 0.1, 16)
    t.setheading(270)  # 画笔角度
    radian_right(1.2, 0.4, 0.1, 25)
    t.setheading(132)  # 画笔角度
    t.forward(31)
    t.end_fill()
    t.begin_fill()
    t.fillcolor("black")
    t.pu()  # 提笔
    t.goto(-88, 141)  # 笔头初始位置
    t.pd()  # 下笔
    t.setheading(145)  # 画笔角度
    radian_left(1.2, 1.6, 0.1, 16)
    t.setheading(270)  # 画笔角度
    radian_left(1.2, 0.4, 0.1, 25)
    t.setheading(48)  # 画笔角度
    t.forward(31)
    t.end_fill()


# 画尾巴
def init_tail():
    # 尾巴
    t.begin_fill()
    t.fillcolor("yellow")
    t.pu()  # 提笔
    t.goto(64, -140)  # 笔头初始位置
    t.pd()  # 下笔
    t.setheading(10)  # 画笔角度
    t.forward(20)
    t.setheading(90)  # 画笔角度
    t.forward(20)
    t.setheading(10)  # 画笔角度
    t.forward(10)
    t.setheading(80)  # 画笔角度
    t.forward(100)
    t.setheading(35)  # 画笔角度
    t.forward(80)
    t.setheading(260)  # 画笔角度
    t.forward(100)
    t.setheading(205)  # 画笔角度
    t.forward(40)
    t.setheading(260)  # 画笔角度
    t.forward(37)
    t.setheading(205)  # 画笔角度
    t.forward(20)
    t.setheading(260)  # 画笔角度
    t.forward(25)
    t.setheading(175)  # 画笔角度
    t.forward(30)
    t.setheading(100)  # 画笔角度
    t.forward(13)
    t.end_fill()


# 画脚
def init_foots():
    # 脚
    t.begin_fill()
    t.fillcolor("yellow")
    t.pensize(2)
    t.pu()  # 提笔
    t.goto(-70, -200)  # 笔头初始位置
    t.pd()  # 下笔
    t.setheading(225)  # 画笔角度
    radian_left(0.5, 1.2, 0, 12)
    radian_left(35, 0.6, 0, 4)
    radian_left(1, 1.2, 0, 18)
    t.setheading(160)  # 画笔角度
    t.forward(13)
    t.end_fill()
    t.begin_fill()
    t.fillcolor("yellow")
    t.pensize(2)
    t.pu()  # 提笔
    t.goto(70, -200)  # 笔头初始位置
    t.pd()  # 下笔
    t.setheading(315)  # 画笔角度
    radian_right(0.5, 1.2, 0, 12)
    radian_right(35, 0.6, 0, 4)
    radian_right(1, 1.2, 0, 18)
    t.setheading(20)  # 画笔角度
    t.forward(13)
    t.end_fill()


# 画身体
def init_body():
    # 外形轮廓
    t.begin_fill()
    t.pu()  # 提笔
    t.goto(112, 0)  # 笔头初始位置
    t.pd()  # 下笔
    t.setheading(90)  # 画笔角度
    t.circle(112, 180)
    t.setheading(250)  # 画笔角度
    radian_left(1.6, 1.3, 0, 50)
    radian_left(0.8, 1.5, 0, 25)
    t.setheading(255)  # 画笔角度
    radian_left(0.4, 1.6, 0.2, 27)
    radian_left(2.8, 1, 0, 45)
    radian_right(0.9, 1.4, 0, 31)
    t.setheading(355)  # 画笔角度
    radian_right(0.9, 1.4, 0, 31)
    radian_left(2.8, 1, 0, 45)
    radian_left(0.4, 7.2, -0.2, 27)
    t.setheading(10)  # 画笔角度
    radian_left(0.8, 1.5, 0, 25)
    radian_left(1.6, 1.3, 0, 50)
    t.end_fill()


def init_eyes():
    # 左眼睛
    t.begin_fill()
    t.fillcolor("black")
    t.pu()  # 提笔
    t.goto(-46, 10)  # 笔头初始位置
    t.pd()  # 下笔
    t.setheading(90)  # 画笔角度
    t.circle(5, 360)
    t.end_fill()
    # 右眼睛
    t.begin_fill()
    t.fillcolor("black")
    t.pu()  # 提笔
    t.goto(46, 10)  # 笔头初始位置
    t.pd()  # 下笔
    t.setheading(-90)  # 画笔角度
    t.circle(5, 360)
    t.end_fill()


# 画脸
def init_face():
    # 脸蛋
    t.begin_fill()
    t.fillcolor("red")
    t.pu()  # 提笔
    t.goto(-63, -10)  # 笔头初始位置
    t.pd()  # 下笔
    t.setheading(90)  # 画笔角度
    t.circle(10, 360)
    t.end_fill()
    t.begin_fill()
    t.fillcolor("red")
    t.pu()  # 提笔
    t.goto(63, -10)  # 笔头初始位置
    t.pd()  # 下笔
    t.setheading(-90)  # 画笔角度
    t.circle(10, 360)
    t.end_fill()
    # 嘴巴
    t.pensize(2.2)
    t.pu()  # 提笔
    t.goto(0, 0)  # 笔头初始位置
    t.pd()  # 下笔
    t.setheading(235)  # 画笔角度
    radian_right(5, 0.8, 0, 30)
    t.pu()  # 提笔
    t.goto(0, 0)  # 笔头初始位置
    t.pd()  # 下笔
    t.setheading(305)  # 画笔角度
    radian_left(5, 0.8, 0, 30)


# 画手
def init_hands():
    # 左手
    t.pensize(2)
    t.pu()  # 提笔
    t.goto(-46, -100)  # 笔头初始位置
    t.pd()  # 下笔
    t.setheading(285)  # 画笔角度
    radian_right(0.4, 1.2, 0, 26)
    radian_right(5, 0.35, 0, 26)
    radian_right(0.3, 1.2, 0, 15)
    # 右手
    t.pu()  # 提笔
    t.goto(46, -100)  # 笔头初始位置
    t.pd()  # 下笔
    t.setheading(255)  # 画笔角度
    radian_left(0.4, 1.2, 0, 26)
    radian_left(5, 0.35, 0, 26)
    radian_left(0.3, 1.2, 0, 15)


def close_eyes():
    # 左眼睛
    t.pu()  # 提笔
    t.goto(-46, 12)  # 笔头初始位置
    t.pd()  # 下笔
    t.setheading(180)  # 画笔角度
    t.forward(10)
    # 右眼睛
    t.pu()  # 提笔
    t.goto(46, 12)  # 笔头初始位置
    t.pd()  # 下笔
    t.setheading(0)  # 画笔角度
    t.forward(10)


def draw_yellow_boy(show_automation_flag: bool, close_eyes_flag: bool):
    if show_automation_flag:
        t.tracer(1, 0)  # 画笔的动画效果
    else:
        t.tracer(0, 0)  # 停止画笔的动画效果, 需要通过update方法手动进行屏幕刷新

    init_ears()
    init_tail()
    init_foots()
    init_body()
    init_face()
    init_hands()
    if close_eyes_flag:
        close_eyes()
    else:
        init_eyes()


def main():
    draw_yellow_boy(show_automation_flag=True, close_eyes_flag=False)
    # 眨眼睛动画
    t.reset()
    t.hideturtle()
    for i in range(30):
        if i % 2 == 0:
            draw_yellow_boy(show_automation_flag=False, close_eyes_flag=True)
            t.update()  # 手动刷新屏幕
            time.sleep(0.3)
        else:
            draw_yellow_boy(show_automation_flag=False, close_eyes_flag=False)
            t.update()  # 手动刷新屏幕
            time.sleep(1)

    t.done()  # 结束画笔


if __name__ == '__main__':
    main()
