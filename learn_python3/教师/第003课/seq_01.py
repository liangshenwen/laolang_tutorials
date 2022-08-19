s1: str = "0123456789"
print(s1[0], "==", s1[-len(s1)])
print(s1[5], "==", s1[-len(s1) + 5])

s_1 = slice(0, 100, 2)
print(s_1.indices(1000))