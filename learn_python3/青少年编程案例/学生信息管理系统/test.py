x = [1, 2, 3]
y = [4, 5, 6]
print('x=', x)
print('y=', y)
x2, y2 = zip(*zip(x, y))
print('x2=', list(x2))
print('y2=', list(y2))
print('x == list(x2) and y == list(y2):', x == list(x2) and y == list(y2))
