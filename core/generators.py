# написать генераторную функцию, которая принимает число N возвращает N рандомных чисел от 1 до 100
from random import randrange
def gen(N):
    for i in range(N):
        yield randrange(1, 100)

N = 10
# написать генераторное выражение, которое делает то же самое
(randrange(1, 100) for i in range(N))
