# 内置dict类型的__getitem__是不支持切片功能
data = {'a': 'hello', 'b': 'world', 'c': '!'}
# TypeError: unhashable type: 'slice'
# print(data[::])


class MyDict:
    def __init__(self):
        self.data = {}

    def __len__(self):
        return len(self.data)

    def append(self, item):
        self.data[len(self)] = item

    def __getitem__(self, key):
        if isinstance(key, int):
            return self.data[key]
        if isinstance(key, slice):
            slice_keys = list(self.data.keys())[key]
            return {k: self.data[k] for k in slice_keys}
        else:
            raise TypeError('Unsupported key type:' + str(type(key)))


my_dict = MyDict()
my_dict.append("My")
my_dict.append("name")
my_dict.append("is")
my_dict.append("007")
print('my_dict[2]->', my_dict[2])
print('my_dict[:2]->', my_dict[:2])
print('my_dict[-4:-1]->', my_dict[-4:-1])
