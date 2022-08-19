import itertools

rng = (x for x in range(5))
print(list(itertools.islice(rng, 3)))
print(list(itertools.islice(rng, 2)))


class Fib:
    def __init__(self):
        self.a, self.b = 1, 1

    def __iter__(self):
        while True:
            yield self.a
            self.a, self.b = self.b, self.a + self.b


f = iter(Fib())
for x in itertools.islice(f, 0, 6):
    print(x, end=" ")
print("\ncontinue")
for x in itertools.islice(f, 0, 6):
    print(x, end=" ")
