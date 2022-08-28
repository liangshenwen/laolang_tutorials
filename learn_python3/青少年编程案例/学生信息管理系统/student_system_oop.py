"""系统运行主界面.
"""
import os
import shelve

# Yes or No 应答选择
YES = ('yes', 'y')
NO = ('no', 'n')

# 学生信息字段
STUDENT_ID = 'id'
STUDENT_NAME = 'name'
STUDENT_SCORE_CHINESE = 'chinese'
STUDENT_SCORE_MATH = 'math'
STUDENT_SCORE_ENGLISH = 'english'

# 成绩最多保持2位小数
SCORE_PRECISION = 2

STUDENT_TXT_FILE = 'students_oop.txt'
STUDENT_SHELVE_FILE = 'students_oop.shelve'

UTF_8 = 'UTF-8'


class Student:
    """学生信息类.
    """
    def __init__(self):
        """无参构造函数"""
        self.id = None
        self.name = None
        self.chinese = None
        self.math = None
        self.english = None

    def to_dict(self):
        """把学生类转换成一个字典"""
        return {
            STUDENT_ID: self.id,
            STUDENT_NAME: self.name,
            STUDENT_SCORE_CHINESE: self.chinese,
            STUDENT_SCORE_MATH: self.math,
            STUDENT_SCORE_ENGLISH: self.english
        }

    @classmethod
    def from_dict(cls, dct):
        """从一个字典构建一个学生类
        """
        stu = cls()
        stu.id = dct[STUDENT_ID]
        stu.name = dct[STUDENT_NAME]
        stu.chinese = dct[STUDENT_SCORE_CHINESE]
        stu.english = dct[STUDENT_SCORE_ENGLISH]
        stu.math = dct[STUDENT_SCORE_MATH]
        return stu


class StudentDao:
    """学生信息访问类"""
    def insert(self, student_lst):
        raise NotImplementedError('请在子类中实现该功能')

    def modify(self, student):
        raise NotImplementedError('请在子类中实现该功能')

    def delete(self, stu_id):
        raise NotImplementedError('请在子类中实现该功能')

    def query(self, by_field, by_value):
        raise NotImplementedError('请在子类中实现该功能')

    def query_all(self):
        raise NotImplementedError('请在子类中实现该功能')


class StudentShelveDao(StudentDao):
    ROWS = 'rows'

    def __init__(self, db_shelve_file=STUDENT_SHELVE_FILE):
        self.db_shelve_file = db_shelve_file

    def insert(self, student_lst):
        insert_flags = []
        """保存学生信息到本地文件.
        """
        stu_db = shelve.open(self.db_shelve_file)
        students_new = []
        if self.ROWS in stu_db:
            students_new.extend(stu_db[self.ROWS])
        # 写入新的学生学生信息
        for student in student_lst:
            existed_flag = False
            for existed_stu in students_new:
                if student.id == existed_stu.id:
                    existed_flag = True
                    break
            if existed_flag:
                insert_flags.append('重复ID-插入失败:' + student.id)
            else:
                students_new.append(student)
                insert_flags.append('插入成功:' + student.id)

        stu_db[self.ROWS] = students_new
        # 关闭文件释放内存
        stu_db.close()
        return insert_flags

    def modify(self, student):
        modify_flg = False
        stu_db = shelve.open(self.db_shelve_file)
        if self.ROWS not in stu_db:
            modify_flg = False
        else:
            students_new = []
            for old_student in stu_db[self.ROWS]:
                if old_student.id == student.id:
                    old_student.name = student.name
                    old_student.chinese = student.chinese
                    old_student.math = student.math
                    old_student.english = student.english
                    modify_flg = True
                students_new.append(old_student)
            stu_db[self.ROWS] = students_new
        # 关闭文件释放内存
        stu_db.close()

        return modify_flg

    def query(self, by_field, by_value):
        student_query = []
        students_old = self.query_all()
        for student_old in students_old:
            # 按照ID进行查找
            if by_field == STUDENT_ID:
                if student_old.id == by_value:
                    student_query.append(student_old)
            # 按照姓名查找
            elif by_field == STUDENT_NAME:
                if student_old.name == by_value:
                    student_query.append(student_old)

        return student_query

    def delete(self, stu_id):
        del_flg = False  # 是否删除标记
        stu_db = shelve.open(self.db_shelve_file)
        if self.ROWS in stu_db:
            students_new = []
            students_old = stu_db[self.ROWS]
            for student_old in students_old:
                if student_old.id == stu_id:
                    del_flg = True
                else:
                    students_new.append(student_old)
            stu_db[self.ROWS] = students_new
        # 关闭文件释放内存
        stu_db.close()

        return del_flg

    def query_all(self):
        student_lst = []
        stu_db = shelve.open(self.db_shelve_file)
        if self.ROWS in stu_db:
            for student in stu_db[self.ROWS]:
                student_lst.append(student)

        # 关闭文件释放内存
        stu_db.close()
        return student_lst


class StudentTxtFileDao(StudentDao):
    """基于文本文件的学生信息访问"""

    def __init__(self, db_txt_file=STUDENT_TXT_FILE):
        self.db_txt_file = db_txt_file

    def insert(self, student_lst):
        """保存学生信息到本地文件.
        """
        insert_flags = []
        # 如果students.txt文件已经存在，采用追加的方式写入新数据, 如果不存在，使用写入方式录入新数据
        if os.path.exists(self.db_txt_file):
            student_txt_file = open(self.db_txt_file, mode='a', encoding=UTF_8)
        else:
            student_txt_file = open(self.db_txt_file, mode='w', encoding=UTF_8)
        students_old = self.query_all()
        # 写入新的学生学生信息
        for student in student_lst:
            existed_flag = False
            for student_old in students_old:
                if student_old.id == student.id:
                    existed_flag = True
                    break
            if existed_flag:
                insert_flags.append('重复ID-插入失败:' + student.id)
            else:
                student_txt_file.write(str(student.to_dict()) + '\n')
                insert_flags.append('插入成功:' + student.id)
                students_old.append(student)
        # 关闭文件释放内存
        student_txt_file.close()
        return insert_flags

    def modify(self, student):
        modify_flg = False
        students_old = self.query_all()
        with open(self.db_txt_file, mode='w', encoding=UTF_8) as f:
            for old_student in students_old:
                if old_student.id == student.id:
                    f.write(str(student.to_dict()) + '\n')
                    modify_flg = True
                else:
                    f.write(str(old_student.to_dict()) + '\n')

        return modify_flg

    def query(self, by_field, by_value):
        student_query = []
        students_old = self.query_all()
        for student_old in students_old:
            # 按照ID进行查找
            if by_field == STUDENT_ID:
                if student_old.id == by_value:
                    student_query.append(student_old)
            # 按照姓名查找
            elif by_field == STUDENT_NAME:
                if student_old.name == by_value:
                    student_query.append(student_old)

        return student_query

    def delete(self, stu_id):
        students_old = self.query_all()

        del_flg = False  # 是否删除标记
        if students_old:
            with open(self.db_txt_file, mode='w', encoding=UTF_8) as f:
                for student_old in students_old:
                    if student_old.id != stu_id:
                        f.write(str(student_old.to_dict()) + '\n')
                    else:
                        del_flg = True
        return del_flg

    def query_all(self):
        student_lst = []
        if os.path.exists(self.db_txt_file):
            # 使用只读模式打开students.txt
            with open(self.db_txt_file, mode='r', encoding=UTF_8) as f:
                students = f.readlines()
                for item in students:
                    student = Student.from_dict(dict(eval(item)))
                    student_lst.append(student)

        return student_lst


class Application:
    def __init__(self, student_dao: StudentDao):
        self.student_dao = student_dao

    def show_menu(self):
        """显示功能菜单.
        """
        print('============================学生信息管理系统=================================')
        print('-------------------------------功能菜单-------------------------------------')
        prefix_blank = '                   '
        print(prefix_blank, '1.录入学生信息')
        print(prefix_blank, '2.查找学生信息')
        print(prefix_blank, '3.删除学生信息')
        print(prefix_blank, '4.修改学生信息')
        print(prefix_blank, '5.根据分数对学生进行排序')
        print(prefix_blank, '6.统计学生总人数')
        print(prefix_blank, '7.显示所有学生信息')
        print(prefix_blank, '0.退出')
        print('---------------------------------------------------------------------------')

    def insert_student(self):
        """插入学生信息模块.
        """
        student_lst = []
        while True:
            stu_id = input('请输入ID(如1001):')
            if not stu_id:
                print('学生ID不能为空，请重新输入!!!')
                continue
            stu_name = input('请输入姓名:')
            if not stu_name:
                print('学生名字不能为空，请重新输入!!!')
                continue
            try:
                chinese_score = round(float(input('请输入语文成绩:')), SCORE_PRECISION)
                math_score = round(float(input('请输入数学成绩:')), SCORE_PRECISION)
                english_score = round(float(input('请输入英语成绩:')), SCORE_PRECISION)
            except:
                print('输入成绩不是浮点数类型，请重新输入!!!')
                continue

            # 使用字典来保存学生数据
            student = Student()
            student.id = stu_id
            student.name = stu_name
            student.chinese = chinese_score
            student.english = english_score
            student.math = math_score

            # 添加到学生列表中
            student_lst.append(student)

            add_more_answer = input('是否继续添加? y/n:')
            if add_more_answer in YES:
                continue
            else:
                break

        # 把学生信息保存到文本文件
        if student_lst:
            insert_flags = self.student_dao.insert(student_lst)
            print(','.join(insert_flags))
            print('学生信息录入完毕!!!')

    def show_students(self, student_lst):
        """根据学生列表展示学生信息.
        """
        if student_lst:
            # 居中对齐
            title_fmt = '{:^6}\t{:^12}\t{:^8}\t{:^8}\t{:^8}\t{:^8}'
            data_fmt = '{:^6}\t{:^12}\t{:^10}\t{:^10}\t{:^10}\t{:^10}'
            # 定义标题
            print(title_fmt.format('ID', '姓名', '语文成绩', '数学成绩', '英语成绩', '总成绩'))
            for student in student_lst:
                # 第一种加总的方式: 多个值通过`+`直接相加
                # sum_score = float(student.chinese) \
                #             + float(student.math) \
                #             + float(student.english)
                # 第二种加总方式: 使用内置函数sum(元组)
                sum_score = sum((float(student.english),
                                 + float(student.math),
                                 + float(student.chinese)))
                sum_score = round(sum_score, SCORE_PRECISION)
                print(data_fmt.format(student.id,
                                      student.name,
                                      student.chinese,
                                      student.math,
                                      student.english,
                                      sum_score))
        else:
            print('没有查询到学生信息，无数据可显示!!!')
            return

    def search_student(self):
        """查找学生信息模块.
        """
        while True:
            stu_id = ''
            stu_name = ''
            mode = input('按ID查找输入1, 按姓名查找输入2:')
            if mode == '1':
                stu_id = input('请输入ID:')
            elif mode == '2':
                stu_name = input('请输入名字:')
            else:
                print('你的输入有误, 请重新输入!!!')
                continue
            student_query = []
            if stu_id:
                student_query = self.student_dao.query(by_field=STUDENT_ID, by_value=stu_id)
            elif stu_name:
                student_query = self.student_dao.query(by_field=STUDENT_NAME, by_value=stu_name)

            if student_query:
                # 显示学生信息
                self.show_students(student_query)

                # 清空查询结果
                student_query.clear()

                search_more_answer = input('是否继续查询学生信息? y/n:')
                if search_more_answer in YES:
                    continue  # 继续查询
                else:
                    break  # 退出查询
            else:
                print('无学生信息!!!')
                return

    def delete_student(self):
        """删除学生信息模块.
        """
        while True:
            stu_id = input('请输入要删除的学生ID:')
            if stu_id:
                del_flg = self.student_dao.delete(stu_id)
                if del_flg:
                    print(f'已经删除ID为{stu_id}学生数据!!!')
                else:
                    print(f'没有找到ID为{stu_id}的数据!!!')
            else:
                print('学生ID不能为空!!!')
                continue

            # 删除之后，重新显示所有学生信息
            self.show_all_students()

            # 是否继续删除学生信息
            del_more_answer = input('是否继续删除学生信息? y/n:')
            if del_more_answer in YES:
                continue
            else:
                break

    def modify_student(self):
        """修改学生信息模块.
        """
        # 显示所有学生信息
        self.show_all_students()

        stu_id = input('请输入要修改的学生ID:')
        students_old = self.student_dao.query(by_field=STUDENT_ID, by_value=stu_id)
        if len(students_old) > 0:
            for student_old in students_old:
                if student_old.id == stu_id:
                    print('找到学生信息，可以修改他的其他信息了!')
                    while True:
                        stu_name = input('请输入姓名(如果为空,将保持旧名字):')
                        if stu_name:
                            student_old.name = stu_name
                        try:
                            chinese_score = input('请输入语文成绩(如果为空,将保持旧成绩):')
                            if chinese_score:
                                student_old.chinese = float(chinese_score)

                            math_score = input('请输入数学成绩(如果为空,将保持旧成绩):')
                            if math_score:
                                student_old.math = float(math_score)

                            english_score = input('请输入英语成绩(如果为空,将保持旧成绩):')
                            if english_score:
                                student_old.english = float(english_score)
                        except:
                            print('输入成绩不是浮点数类型，请重新输入!!!')
                            continue
                        modify_flg = self.student_dao.modify(student_old)
                        if modify_flg:
                            print('修改成功!!!')
                        else:
                            print('修改失败!!!')
                        break
        else:
            print('无法找到学生信息!!!')

        modify_more_answer = input('是否继续修改其他学生信息? y/n:')
        if modify_more_answer in YES:
            self.modify_student()
        else:
            return

    def sort_students_by_score(self):
        """根据成绩对学生信息进行排序模块.
        """
        student_lst = self.student_dao.query_all()
        if len(student_lst) > 0:
            while True:
                reverse_flg = False
                asc_or_desc = input('请选择(0-升序, 1-降序, -1-退出排序):')
                if asc_or_desc == '0':
                    reverse_flg = False
                elif asc_or_desc == '1':
                    reverse_flg = True
                elif asc_or_desc == '-1':
                    print('退出排序')
                    return
                else:
                    print('你的输入有误, 请重新输入!!!')
                    continue

                mode = input('请选择排序方式(1-按英语成绩排序, 2-按语文成绩排序, 3-按数学成绩排序, 0-按总成绩排序, -1-退出排序):')
                # list.sort方法默认是按照升序，我们通过reverse标志位来控制是否按照降序
                if mode == '1':
                    # 排序方式 1: 使用内置函数sorted(学历,key,reverse)
                    # student_lst = sorted(student_lst, key=lambda x: float(x.english),
                    #                      reverse=reverse_flg)
                    # 排序方式 2: 使用sorted()和reversed(), sorted()如果不指定reverse参数，默认会按照升序
                    # student_lst = sorted(student_lst, key=lambda x: float(x.english))
                    # if reverse_flg:
                    #     student_lst = reversed(student_lst)
                    # 排序方式 3: 使用list的sort方法
                    student_lst.sort(key=lambda x: float(x.english), reverse=reverse_flg)
                elif mode == '2':
                    student_lst.sort(key=lambda x: float(x.chinese), reverse=reverse_flg)
                elif mode == '3':
                    student_lst.sort(key=lambda x: float(x.math), reverse=reverse_flg)
                elif mode == '0':
                    student_lst.sort(key=lambda x: round(float(x.math) +
                                                         float(x.english) +
                                                         float(x.chinese), SCORE_PRECISION),
                                     reverse=reverse_flg)
                elif mode == '-1':
                    print('退出排序')
                    return
                else:
                    print('你的输入有误, 请重新输入!!!')
                    continue

                break

            self.show_students(student_lst)

        else:
            print('当前还没有录入任何学生信息!!!')
            return

    def sum_students(self):
        """统计学生信息模块.
        """
        students_old = self.student_dao.query_all()
        if students_old:
            print(f'一共有{len(students_old)}名学生')
        else:
            print('当前还没有录入任何学生信息!!!')

    def show_all_students(self):
        """展示所有学生信息模块.
        """
        student_lst = self.student_dao.query_all()
        if student_lst:
            self.show_students(student_lst)
        else:
            print('当前还没有录入任何学生信息!!!')


def main():
    """学生信息管理系统主应用程序.
    """
    # student_dao = StudentTxtFileDao()
    student_dao = StudentShelveDao()
    app = Application(student_dao)

    while True:
        app.show_menu()
        menu_choice = int(input('请选择功能菜单:'))
        if menu_choice in [0, 1, 2, 3, 4, 5, 6, 7]:
            if menu_choice == 0:
                quit_answer = input('你确定退出系统吗? y/n:').lower()
                if quit_answer in YES:
                    print('感谢您的使用!!')
                    # 退出系统
                    break
                else:
                    # 继续使用系统
                    continue
            elif menu_choice == 1:
                # 录入学生信息
                app.insert_student()
            elif menu_choice == 2:
                # 查找学生信息
                app.search_student()
            elif menu_choice == 3:
                # 删除学生信息
                app.delete_student()
            elif menu_choice == 4:
                # 修改学生信息
                app.modify_student()
            elif menu_choice == 5:
                # 根据分数来对学生进行排序
                app.sort_students_by_score()
            elif menu_choice == 6:
                # 统计学生总人数
                app.sum_students()
            elif menu_choice == 7:
                # 显示所有学生信息
                app.show_all_students()


if __name__ == '__main__':
    main()
