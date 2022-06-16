"""
https://www.runoob.com/matplotlib/matplotlib-subplots.html

设置 numRows ＝ 1，numCols ＝ 2，就是将图表绘制成 1x2 的图片区域, 对应的坐标为：

(1, 1), (1, 2)
plotNum ＝ 1, 表示的坐标为(1, 1), 即第一行第一列的子图。

plotNum ＝ 2, 表示的坐标为(1, 2), 即第一行第二列的子图。

"""
import matplotlib.pyplot as plt
import numpy as np
# plot 1:
xpoints = np.array([0, 6])
ypoints = np.array([0, 100])

plt.subplot(1, 2, 1)
plt.plot(xpoints, ypoints)
plt.title("plot 1")

# plot 2:
x = np.array([1, 2, 3, 4])
y = np.array([1, 4, 9, 16])

plt.subplot(1, 2, 2)
plt.plot(x, y)
plt.title("plot 2")

plt.suptitle("RUNOOB subplot Test")

plt.show()
