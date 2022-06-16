"""
https://www.runoob.com/matplotlib/matplotlib-subplots.html

subplots()
subplots() 方法语法格式如下：

matplotlib.pyplot.subplots(nrows=1, ncols=1, *, sharex=False, sharey=False, squeeze=True, subplot_kw=None, gridspec_kw=None, **fig_kw)参数说明：
nrows：默认为 1，设置图表的行数。
ncols：默认为 1，设置图表的列数。
sharex、sharey：设置 x、y 轴是否共享属性，默认为 false，可设置为 'none'、'all'、'row' 或 'col'。 False 或 none 每个子图的 x 轴或 y 轴都是独立的，True 或 'all'：所有子图共享 x 轴或 y 轴，'row' 设置每个子图行共享一个 x 轴或 y 轴，'col'：设置每个子图列共享一个 x 轴或 y 轴。
squeeze：布尔值，默认为 True，表示额外的维度从返回的 Axes(轴)对象中挤出，对于 N*1 或 1*N 个子图，返回一个 1 维数组，对于 N*M，N>1 和 M>1 返回一个 2 维数组。如果设置为 False，则不进行挤压操作，返回一个元素为 Axes 实例的2维数组，即使它最终是1x1。
subplot_kw：可选，字典类型。把字典的关键字传递给 add_subplot() 来创建每个子图。
gridspec_kw：可选，字典类型。把字典的关键字传递给 GridSpec 构造函数创建子图放在网格里(grid)。
**fig_kw：把详细的关键字参数传给 figure() 函数。
"""
import matplotlib.pyplot as plt
import numpy as np

# 创建一些测试数据
x = np.linspace(0, 2*np.pi, 400)
y = np.sin(x**2)

# 创建一个画像和子图  -- 图1
# fig, ax = plt.subplots()
# ax.plot(x, y)
# ax.set_title('Simple plot')

# 创建两个子图 -- -- 图2
# fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
# ax1.plot(x, y)
# ax1.set_title('Sharing Y axis')
# ax2.scatter(x, y)

# 创建四个子图 -- 图3
# fig, axs = plt.subplots(2, 2, subplot_kw=dict(projection="polar"))
# fig, axs = plt.subplots(2, 2)
# axs[0, 0].plot(x, y)
# axs[1, 1].scatter(x, y)

# 共享 x 轴 -- 图4
# plt.subplots(2, 2, sharex='col')

# 共享 y 轴  -- 图5
# plt.subplots(2, 2, sharey='row')

# 共享 x 轴和 y 轴 -- 图6
# plt.subplots(2, 2, sharex='all', sharey='all')

# 这个也是共享 x 轴和 y 轴 -- 图7
# plt.subplots(2, 2, sharex=True, sharey=True)

# 创建第8号图，已经存在的则删除 -- 图8
fig, ax = plt.subplots(num=8, clear=True)
ax.plot(x, y)
ax.set_title('pic 8 - 1')
# 创建第8号图，已经存在的则不删除 -- 图8
fig, ax = plt.subplots(num=8, clear=False)
ax.scatter(x, y)
ax.set_title('pic 8 - 2')
plt.show()
