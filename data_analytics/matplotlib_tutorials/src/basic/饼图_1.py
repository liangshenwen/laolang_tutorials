"""
https://www.runoob.com/matplotlib/matplotlib-pie.html
我们可以使用 pyplot 中的 pie() 方法来绘制饼图。

注意：默认情况下，第一个扇形的绘制是从 x 轴开始并逆时针移动。
"""

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])

plt.pie(y,
        labels=['A', 'B', 'C', 'D'],  # 设置饼图标签
        colors=["#d5695d", "#5d8ca8", "#65a479", "#a564c9"],  # 设置饼图颜色
        explode=(0, 0.2, 0, 0),  # 第二部分突出显示，值越大，距离中心越远
        autopct='%.2f%%',  # 格式化输出百分比
        )
plt.title("RUNOOB Pie Test")

plt.show()
