import inspect
from collections.abc import Sequence, MutableSequence, Set

print(inspect.getmro(list))

# 列表
l_1 = [1, 2, 3, 4]
print(l_1)

s_1 = {1, 2, 3, 4, 5, 4}
print(s_1)
print(inspect.getmro(Set))

print(isinstance(s_1, Set))
print(isinstance(s_1, Sequence))
print(isinstance(s_1, MutableSequence))