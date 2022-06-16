"""
https://www.runoob.com/matplotlib/matplotlib-line.html
"""

import matplotlib.pyplot as plt
import numpy as np

y_points = np.array([6, 2, 13, 10])

# 线的类型
# 线的类型可以使用 linestyle 参数来定义，简写为 ls。
# plt.plot(y_points, linestyle='dotted')

# plt.plot(y_points, ls='-.')

# 线的颜色可以使用 color 参数来定义，简写为 c。
plt.plot(y_points, color='red')
# plt.plot(y_points, c='#8FBC8F')

# 线的宽度
# 线的宽度可以使用 linewidth 参数来定义，简写为 lw，值可以是浮点数，如：1、2.0、5.67 等。

# plt.plot(y_points, linewidth='12.5')
# plt.plot(y_points, lw='12.5')

# 多条线
# plot() 方法中可以包含多对 x,y 值来绘制多条线。
y1 = np.array([3, 7, 5, 9])
y2 = np.array([6, 2, 13, 10])

# x 的值默认设置为 [0, 1, 2, 3]。
# plt.plot(y1)
# plt.plot(y2)

# 我们也可以自己设置 x 坐标等值：
x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 7, 5, 9])
x2 = np.array([4, 5, 6, 7])
y2 = np.array([6, 2, 13, 10])

plt.plot(x1, y1, x2, y2)

plt.show()
