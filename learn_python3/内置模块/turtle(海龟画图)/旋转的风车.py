# 案例6：绘制旋转的风车

# ①程序初始化设置
import turtle  # 导入turtle库（模块）

turtle.bgpic("风车背景.gif")  # 导入一张gif图片做背景
turtle.title('旋转的风车')
turtle.tracer(0)  # 没有画图过程，图形会立马呈现出最终结果    

# ②变量初始化设置
# 分别创建深色和浅色列表
dark_color = ["#267fb9", "#f2b11b", "#538a30", "#ba62c1"]  # 深色列表
light_color = ["#2aaad1", "#f3d727", "#7fbc2b", "#cc81d2"]  # 浅色列表
# b1是大等腰直角三角形的斜边，a1是直角边
b1 = 150  # 只要改变b1的值，风车的大小会等比例缩放
a1 = 2 ** 0.5 / 2 * b1  # 2**0.5 表示数学中的“根号2”
# b2是小等腰直角三角形的斜边，a2是直角边
a2 = b1 / 2
b2 = 2 ** 0.5 * a2
# 设置风车杆的长度和宽度
length = 1.7 * b1
width = 2 / 15 * b1

# ③起始坐标上移
turtle.penup()
turtle.goto(0, 70)
turtle.pendown()

# ④自定义函数fun()
turtle.right(22)  # 向右旋转22度后再画风车，加一定的角度，风车比较有动感


def fun():
    """
    函数功能：每调用一次fun()，就会在旋转1度后的新方向出现风车 
    """
    turtle.clear()
    turtle.right(1)
    for i in range(4):
        # 画小的等腰直角三角形
        turtle.color(dark_color[i])  # 遍历深色列表dark_color
        turtle.begin_fill()
        turtle.forward(a2)
        turtle.left(90)
        turtle.forward(a2)
        turtle.left(135)
        turtle.forward(b2)
        turtle.end_fill()

        # 画大的等腰直角三角形
        turtle.color(light_color[i])  # 遍历浅色列表light_color
        turtle.begin_fill()
        turtle.backward(b2)
        turtle.right(90)
        turtle.forward(a1)
        turtle.left(135)
        turtle.forward(b1)
        turtle.end_fill()

        # 旋转180度后，开始画下一片风车叶片
        turtle.right(180)


# ⑤主程序
for j in range(360):  # 让风车旋转80次
    turtle.ontimer(fun, t=50 * (j + 1))  # 安装一个计时器，t毫秒后调用fun()函数

# ⑥绘图结束，隐藏海龟
turtle.hideturtle()

turtle.done()