# if..elif..else
# 把学生的成绩分成4个等级(不及格，及格，良好，优秀)
print('把学生的成绩分成4个等级(不及格，及格，良好，优秀) ================')
score = 10

if score < 60:
    print('不及格')
elif 60 <= score < 75:
    print('及格')
elif 75 <= score < 85:
    print('良好')
else:
    print('优秀')

# while...else
# 计算 1 到 100的和
print('使用while来计算 1 到 100的和 ================')
i = 1  # 变量值
total = 0  # 保存结果
while i <= 100:
    total = total + i
    i = i + 1
else:
    print('计算完毕')

print('1到100所有数相加的和=', total)

# for/in...else
# 计算 1 到 100的和
print('使用for/in来计算 1 到 100的和 ================')
total = 0  # 保存结果
# https://docs.python.org/zh-cn/3/library/stdtypes.html#range
values = list(range(1, 101, 1))
# help(range)
print(values)
for i in values:
    total = total + i
else:
    print('计算完毕')

print('1到100所有数相加的和=', total)

# continue
# 只打印及格的同学的成绩
print('只打印及格的同学的成绩 ================')
scores = [45, 77, 23, 88, 90]
for score in scores:
    if score<60:
        continue  # 不在执行后面的语句，并进入下一个循环
    print('分数为=', score)


# break
# 猜数字游戏
print('猜数字游戏 ================')
lucky_digit = 8
while True:
    guess_digit = int(input('你猜的数字是:'))
    if guess_digit == lucky_digit:
        print('你猜对啦')
        break  # 猜对之后，就退出while循环

