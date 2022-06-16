"""
https://www.runoob.com/matplotlib/matplotlib-scatter.html

我们可以使用 pyplot 中的 scatter() 方法来绘制散点图。
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([1, 4, 9, 16, 7, 11, 23, 18])
fig, ax = plt.subplots(1, 1)
ax.scatter(x, y)

x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([1, 4, 9, 16, 7, 11, 23, 18])
sizes = np.array([20, 50, 100, 200, 500, 1000, 60, 90])
fig, ax = plt.subplots(1, 1)
ax.scatter(x, y, s=sizes)

x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([1, 4, 9, 16, 7, 11, 23, 18])
colors = np.array(["red", "green", "black", "orange", "purple", "beige", "cyan", "magenta"])
fig, ax = plt.subplots(1, 1)
ax.scatter(x, y, c=colors)

fig, ax = plt.subplots(1, 1)
x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])
ax.scatter(x, y, color='hotpink')

x = np.array([2, 2, 8, 1, 15, 8, 12, 9, 7, 3, 11, 4, 7, 14, 12])
y = np.array([100, 105, 84, 105, 90, 99, 90, 95, 94, 100, 79, 112, 91, 80, 85])
ax.scatter(x, y, color='#88c999')
ax.set_title('ABC')

fig, ax = plt.subplots(1, 1)
# 随机数生成器的种子
np.random.seed(19680801)

N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = (30 * np.random.rand(N)) ** 2  # 0 to 15 point radii

ax.scatter(x, y, s=area, c=colors, alpha=0.5)  # 设置颜色及透明度

ax.set_title("RUNOOB Scatter Test")  # 设置标题

plt.show()
