# 建立表头
print('  |', end='')
for k in range(1, 10):
    # 不自动换行，只保留空格符
    # https://docs.python.org/zh-cn/3/library/string.html#formatstrings
    # 右对齐
    print('{0:>3d}'.format(k), end='')
# 换行
print()
print('-' * 32)
# 第一层 for/in
for one in range(1, 10):
    print(one, '|', end='')
    # 第二层for/in
    for two in range(1, 10):
        # 右对齐
        print('{0:>3d}'.format(one * two), end='')
    # 换行
    print()
