"""
https://www.runoob.com/matplotlib/matplotlib-marker.html

"""
import matplotlib.pyplot as plt
import matplotlib.markers as markers
import numpy as np

y_points = np.array([1, 3, 4, 5, 8, 9, 6, 1, 3, 4, 5, 2, 4])

# plt.plot(y_points, marker='o')
# plt.plot(y_points, marker='*')
# plt.plot(y_points, marker=markers.CARETUP)

# fmt = '[marker][line][color]'
# 例如 o:r，o 表示实心圆标记，: 表示虚线，r 表示颜色为红色。
# plt.plot(y_points, 'o:r')

# 标记大小与颜色
# 我们可以自定义标记的大小与颜色，使用的参数分别是：
# markersize，简写为 ms：定义标记的大小。
# markerfacecolor，简写为 mfc：定义标记内部的颜色。
# markeredgecolor，简写为 mec：定义标记边框的颜色。
plt.plot(y_points, marker='o', ms=20, mec='r', mfc='b')
plt.show()
