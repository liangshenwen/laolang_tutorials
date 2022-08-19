print("--------通过位置参数列表")
print("{} {}".format("hello", "world"))  # 不设置指定位置，按默认顺序
print("{0} {1}".format("hello", "world"))  # 设置指定位置
print("{1} {0} {1}".format("hello", "world"))  # 设置指定位置
lst = ["hello", "world"]
print("{1} {0} {1}".format(*lst)) # 设置指定位置

print("--------通过字典设置参数")
print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.xxx.com"))
# 通过字典设置参数
site = {"name": "菜鸟教程", "url": "www.xxx.com"}
print("网站名：{name}, 地址 {url}".format(**site))

print("--------通过列表索引设置参数")
# 通过列表索引设置参数
my_list = ['菜鸟教程', 'www.xxx.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的

print("--------也可以向 str.format() 传入对象")

class AssignValue(object):
    def __init__(self, value):
        self.value = value
my_value = AssignValue(6)
print('value 为: {0.value}'.format(my_value))  # "0" 是可选的