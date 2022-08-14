import inspect

s1:str = 'abcd'
print(s1)
# s1[0:1] = 'n'
print(s1)
print(inspect.getmro(str))
t1:tuple = (1, 2, 3)
# t1.append(1)
print(type(t1))

print(inspect.getmro(tuple))


