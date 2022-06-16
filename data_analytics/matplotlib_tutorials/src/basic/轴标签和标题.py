"""
https://www.runoob.com/matplotlib/matplotlib-label.html
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib

x = np.array([1, 2, 3, 4])
y = np.array([1, 4, 9, 16])
plt.plot(x, y)

# 我们可以使用 xlabel() 和 ylabel() 方法来设置 x 轴和 y 轴的标签。
# plt.xlabel("x - label")
# plt.ylabel("y - label")

# 我们可以使用 title() 方法来设置标题。
# plt.title("TEST TITLE")

# Matplotlib 默认情况不支持中文，我们可以使用以下简单的方法来解决。

# 查看使用系统的字体
ttf_fonts = sorted([(f.name, f.fname) for f in matplotlib.font_manager.fontManager.ttflist])
for ttf in ttf_fonts:
    print(ttf)
    pass

# https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams
# 通过修改matplotlib的全局参数来实现中文显示的   (验证了在window系统下并不生效)
# plt.rcParams['font.family'] = 'serif'
# plt.rcParams['font.serif'] = 'simsun'
font_options = {
    'family': 'serif',  # 设置字体家族
    'serif': 'SimSun',  # 设置字体
}
# plt.rc('font', **font_options)
print('font.family:', plt.rcParams['font.family'])
print('font.serif:', plt.rcParams['font.serif'])
# fname 为你字体库路径, simsun.ttc为简体中文, size 参数设置字体大小
zh_font1 = matplotlib.font_manager.FontProperties(fname="C:\\Windows\\Fonts\\simsun.ttc", size=18)

# 此外我们还可以自定义字体的样式
font1 = {'color': 'blue', 'size': 20}
font2 = {'color': 'darkred', 'size': 15}

# 标题与标签的定位
# title() 方法提供了 loc 参数来设置标题显示的位置，可以设置为: 'left', 'right', 和 'center'， 默认值为 'center'。
#
# xlabel() 方法提供了 loc 参数来设置 x 轴显示的位置，可以设置为: 'left', 'right', 和 'center'， 默认值为 'center'。
#
# ylabel() 方法提供了 loc 参数来设置 y 轴显示的位置，可以设置为: 'bottom', 'top', 和 'center'， 默认值为 'center'。
x = np.arange(1, 11)
y = 2 * x + 5
plt.title("菜鸟教程 - 测试", fontproperties=zh_font1, fontdict=font1, loc="left")
# plt.title("菜鸟教程 - 测试")
# fontproperties 设置中文显示，fontdict 设置字体样式属性
plt.xlabel("x 轴", fontproperties=zh_font1, fontdict=font2, loc='left')
plt.ylabel("y 轴", fontproperties=zh_font1, fontdict=font2, loc='top')
plt.plot(x, y)

plt.show()
