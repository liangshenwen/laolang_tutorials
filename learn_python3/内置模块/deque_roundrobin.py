# 一个 轮询调度器 可以通过在 deque 中放入迭代器来实现。值从当前迭代器的位置0被取出并暂存(yield)。 如果这个迭代器消耗完毕，就用 popleft()
# 将其从对列中移去；否则，就通过 rotate() 将它移到队列的末尾
from collections import deque


def roundrobin(*iterables):
    "roundrobin('ABC', 'D', 'EF') --> A D E B F C"
    iterators = deque(map(iter, iterables))
    while iterators:
        try:
            while True:
                yield next(iterators[0])
                iterators.rotate(-1)
        except StopIteration:
            # Remove an exhausted iterator.
            iterators.popleft()


for i in roundrobin('ABC', 'D', 'EF'):
    print(i)
