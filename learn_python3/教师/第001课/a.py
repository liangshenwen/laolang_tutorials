# continue
# 只打印及格的同学的成绩
print('只打印及格的同学的成绩 ================')
scores = [45, 77, 23, 88, 90]
for score in scores:
    if score < 60:
        continue  # 不在执行后面的语句，并进入下一个循环
    print('分数为=', score)