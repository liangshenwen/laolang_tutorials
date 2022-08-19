# https://docs.python.org/zh-cn/3/library/string.html#formatstrings

print('----------- 对齐方式')
for k in range(1, 10):
    # 不自动换行，只保留空格符
    # 右对齐
    print('{0:>3d}'.format(k), end='')

print()
for k in range(1, 10):
    # 不自动换行，只保留空格符
    # 左对齐
    print('{0:<3d}'.format(k), end='')

print()
for k in range(1, 10):
    # 不自动换行，只保留空格符
    # 中间对齐
    print('{0:^3d}'.format(k), end='')
print()

for k in range(1, 10):
    # 不自动换行，只保留空格符
    # 中间对齐
    print('{0:03d}'.format(k), end=',')
print()

print('------ 各种进制数的表示')
width = 5
print('十进制  16进制 16进制 八进制 二进制', end='')
print()
for num in range(5, 12):
    for base in 'dxXob':
        print('{0:{width}{base}}'.format(num, base=base, width=width), end=' ')
    print()

print('------  百分数')
points = 19
total = 22
print('Correct answers: {:.2%}'.format(points/total))

print('------- 使用逗号或者_作为千位分隔符')

print('{:,}'.format(1234567890))
print('{:_}'.format(1234567890))

print('------------大括号转义')
print ("{} 对应的位置是 {{0}}".format("laolang"))

print('--------------转换镖旗')
print("Harold's a clever {0!s}".format(1231))        # Calls str() on the argument first
print("Bring out the holy {name!r}".format(name=('lao','lang')))    # Calls repr() on the argument first
print("More {!a}".format('a'))                      # Calls ascii() on the argument first