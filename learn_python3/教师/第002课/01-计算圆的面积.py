"""
圆的计算公式为 area=πr²
"""

import math

# 这里input的是字符串
r = input('请输出圆的半径:')
# 转换成整型
r = int(r)

print('π=', math.pi)

# 计算圆的面积
# area = r * r * math.pi
# area = math.pow(r, 2) * math.pi
area = r**2 * math.pi

print('半径为', r, '的圆的面积为', area)

# 关于python中的math标准库
# https://docs.python.org/zh-cn/3/library/math.html