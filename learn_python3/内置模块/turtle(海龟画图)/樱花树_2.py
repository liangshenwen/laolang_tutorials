import turtle as t
import random as r

t.title('樱花树')
t.ht()  # 隐藏画笔
t.bgcolor("#FFECED")  # 设置背景颜色
t.speed(0)  # 设置画笔速度，0最快，1-10渐进
t.tracer(1, 0)  # 控制绘制动画速度，不加会很慢

# 找到绘画初始点
t.pu()  # 抬笔
t.left(90)
t.bk(300)


# 画枝干
def tree(n, l):
    # n代表分支数，l代表每一节枝干长度
    t.pencolor("#7E373D")  # 画笔颜色
    t.pd()  # 下笔
    t.pensize(n)  # 画笔尺寸
    t.fd(l)
    if n > 0:
        branch_r = 15 * r.random() + 15  # 右分支偏转角度
        branch_l = 15 * r.random() + 15  # 左分支偏转角度
        d = l * (r.random() * 0.25 + 0.65)  # 分支长度
        t.right(branch_r)
        tree(n - 1, d)
        t.left(branch_l + branch_r)
        tree(n - 1, d)
        t.right(branch_l)
    else:
        # 加点圈圈表示树叶
        t.pencolor("#F67A9C")
        t.right(90)
        t.circle(2.5)
        t.left(90)
    t.pu()
    t.bk(l)


tree(7, 100)

t.done()
