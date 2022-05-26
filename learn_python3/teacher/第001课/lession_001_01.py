"""学习定义变量和方法.

有2个中学生均来自`二中七年级21班`, 一个叫张小二， 一个叫王翠花。
首先定义2个学生的基本信息和一个打印学生的相关信息的函数，然后把
"""
# 定义的学生`张小二`的基本信息
stu_name_1: str = '张小二'  # 我的名字叫张小二
stu_age_1: int = 14  # 我的年龄为14岁
stu_sex_1: str = '男'  # 我的性别为男
stu_height_1: float = 171.5  # 我的身高170.5厘米
stu_weight_1: float = 60  # 我的体重60公斤
stu_grade_1: str = '二中七年级21班'
stu_scores_1: [float] = [98.5, 90.0, 100.0]  # 我的数学成绩是98.5分,英语成绩是90分,语文成绩是100分

# 定义的学生`翠花`的基本信息
stu_name_2: str = '王翠花'  # 我的名字叫王翠花
stu_age_2: int = 14  # 我的年龄为14岁
stu_sex_2: str = '女'  # 我的性别为女
stu_height_2: float = 151.5  # 我的身高151.5厘米
stu_weight_2: float = 50  # 我的体重50公斤
stu_grade_2: str = '二中七年级21班'
stu_scores_2: [float] = [70.5, 89.5, 80.1]  # 我的数学成绩是98.5分,英语成绩是90分,语文成绩是100分


# 定义一个打印学生信息的函数
def print_stu_info(name: str, age: int, sex: str, height: float, weight: float, grade: str, scores: [float]):
    print('我的名字叫', name)
    print('我的年龄是', age)
    print('我的性别是', sex)
    print('我的身高是', height)
    print('我的体重是', weight)
    print('我的班级是', grade)
    print('我的三大主科分数分别', '数学=', scores[0], '英语=', scores[1], '语文=', scores[2])


if __name__ == '__main__':
    print('打印第一个学生的基本信息')
    print_stu_info(stu_name_1, stu_age_1, stu_sex_1, stu_height_1, stu_weight_1, stu_grade_1, stu_scores_1)
    print('打印第二个学生的基本信息')
    print_stu_info(stu_name_2, stu_age_2, stu_sex_2, stu_height_2, stu_weight_2, stu_grade_2, stu_scores_2)
