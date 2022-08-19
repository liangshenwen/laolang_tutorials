print('str.__getitem__', '__getitem__' in dir(str))
print('range.__getitem__', '__getitem__' in dir(range))
print('tuple.__getitem__', '__getitem__' in dir(tuple))
print('list.__getitem__', '__getitem__' in dir(list))
print('set.__getitem__', '__getitem__' in dir(set))
# dict虽然支持__getitem__方法，但是它只支持根据key来获取对应的value
print('dict.__getitem__', '__getitem__' in dir(dict))

print('str.__setitem__', '__setitem__' in dir(str))
print('range.__setitem__', '__setitem__' in dir(range))
print('tuple.__setitem__', '__setitem__' in dir(tuple))
print('list.__setitem__', '__setitem__' in dir(list))
print('set.__setitem__', '__setitem__' in dir(set))
# dict虽然支持__setitem__方法，但是它只支持根据key来更新对应的value
print('dict.__setitem__', '__setitem__' in dir(dict))