from sys import setrecursionlimit

setrecursionlimit(100000)


def func(n):
    if n >= 10000:
        return n
    elif n < 10000 and n % 2 == 0:
        return func(n + 2) - 3
    elif n < 10000 and n % 2 != 0:
        return func(n + 2) + 1


print(func(94) - func(80))
