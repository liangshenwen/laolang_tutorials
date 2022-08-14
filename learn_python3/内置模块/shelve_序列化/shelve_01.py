"""
"Shelf" 是一种持久化的类似字典的对象。 与 "dbm" 数据库的区别在于 Shelf 中的值（不是键！）实际上可以为任意 Python 对象 --- 即 pickle 模块能够处理的任何东西。

python之shelve模块详解 https://www.cnblogs.com/sui776265233/p/9225164.html
"""
# 七、代码示例
# 1.创建一个shelf对象，直接使用open函数即可

import shelve
s = shelve.open('test_shelf.db')         #
try:
    s['kk'] = {'int': 10, 'float': 9.5, 'String': 'Sample data'}
    s['MM'] = [1, 2, 3]
finally:
    s.close()

# 2.如果想要再次访问这个shelf，只需要再次shelve.open()就可以了，然后我们可以像使用字典一样来使用这个shelf

import shelve
try:
    s = shelve.open('test_shelf.db')
    value = s['kk']
    print(value)
finally:
    s.close()

# 3.对shelf对象，增、删、改操作

import shelve
s = shelve.open('test_shelf.db', flag='w', writeback=True)
try:
    # 增加
    s['QQQ'] = 2333
    # 删除
    del s['MM']
    # 修改
    s['kk'] = {'String': 'day day up'}
finally:
    s.close()

# 注意：flag设置为‘r’-只读模式，当程序试图去修改一个以只读方式打开的DB时，将会抛一个访问错误的异常。异常的具体类型取决于anydbm这个模块在创建DB时所选用的DB。异常举例：anydbm.error: need ‘c’ or ‘n’ flag to open new db

# 4.循环遍历shelf对象

import shelve
s = shelve.open('test_shelf.db')
try:
    # 方法一：
    for item in s.items():
        print ('键[{}] = 值[{}]'.format(item[0], s[item[0]]))
    # 方法二：
    for key, value in s.items():
        print(key, value)
finally:
    s.close()

# 5.备注一个错误：
# open中的参数filename，起初认为需要手动新建一个.db，或者.dat的文件，目前电脑中无任何真正的数据库文件，所以采用了新建txt文件，修改后缀的方法创建.db，或者.dat的文件。
# 解释器报错，提示内容为："anydbm.error: db type could not be determined"，
# 原因是是filename已经存在，并且格式与shelve不符，所以提示 “db type could not be determined”。
# 解决方法是，删除该文件。首次运行后会自动生成该filename文件。
# 6.稍微复杂些的案例，实现一个简单提问式的数据库

# encoding:utf-8
# 2018/3/8

# 简单的数据库

import sys,shelve

def print_help():
    '存储（增加）、查找、更新（修改）、循环打印、删除、退出、帮助'
    print('The available commons are: ')
    print('store    : Stores information about a person')
    print('lookup   : Looks up a person from ID numbers')
    print("update   : Update a person's information from ID number")
    print('print_all: Print all informations')
    print("delete   : Delete a person's information from ID number")
    print('quit     : Save changes and exit')
    print('?        : Print this message')


def store_people(db):
    pid = input('Please enter a unique ID number: ')
    person = {}
    person['name'] = input('Please enter the name: ')
    person['age'] = input('Please enter the age: ')
    person['phone'] = input('Please enter the phone: ')
    db[pid] = person
    print("Store information: pid is %s, information is %s" % (pid, person))


def lookup_people(db):
    pid = input('Please enter the number: ')
    field = input('What would you like to know? (name, age, phone) ')
    if pid in db.keys():
        value = db[pid][field]
        print("Pid %s's %s is %s" % (pid, field, value))
    else:
        print('Not found this number')


def update_people(db):
    pid = input('Please enter the number: ')
    field = input('What would you like to update? (name, age, phone)  ')
    newvalue = input('Enter the new information: ')
    if pid in db.keys():
        value = db[pid]
        value[field] = newvalue
        print("Pid %s's %s update information is %s" % (pid, field, newvalue))
    else:
        print("Not found this number, can't update")


def delete_people(db):
    pid = input('Please enter the number: ')
    if pid in db.keys():
        del db[pid]
        print("pid %s's information delete done" % pid)
    else:
        print( "Not found this number, can't delete")

def print_all_people(db):
    print( 'All information are: ')
    for key, value in db.items():
        print(key, value)

def enter_cmd():
    cmd = input('Please enter the cmd(? for help): ')
    cmd = cmd.strip().lower()
    return cmd

def main():
    database = shelve.open('database201803.dat', writeback=True)
    try:
        while True:
            cmd = enter_cmd()
            if cmd == 'store':
                store_people(database)
            elif cmd == 'lookup':
                lookup_people(database)
            elif cmd == 'update':
                update_people(database)
            elif cmd == 'print_all':
                print_all_people(database)
            elif cmd == 'delete':
                delete_people(database)
            elif cmd == '?':
                print_help()
            elif cmd == 'quit':
                return
    finally:
        database.close()

if __name__ == '__main__':
    main()