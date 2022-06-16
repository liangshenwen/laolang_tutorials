"""
https://www.runoob.com/matplotlib/matplotlib-bar.html
我们可以使用 pyplot 中的 bar() 方法来绘制柱形图。

设置柱形图宽度，bar() 方法使用 width 设置，barh() 方法使用 height 设置 height
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["Runoob-1", "Runoob-2", "Runoob-3", "C-RUNOOB"])
y = np.array([12, 22, 6, 18])

# plt.bar(x, y, color = ["#4CAF50","red","hotpink","#556B2F"], width = 0.1)
plt.barh(x, y, color="#4CAF50", height=0.1)  # 垂直方向的柱形图可以使用 barh() 方法来设置
plt.show()
