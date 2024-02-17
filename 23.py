def F(x, y):  # Trajectory: exclude 14, include 10
    if x == y:
        return 1
    if x > y or x == 14:
        return 0
    if x < y:
        return F(x + 1, y) + F(x + 2, y) + F(x * 3, y)


print(F(2, 10) * F(10, 15))


def F(x, y):  # Trajectory: include 10
    if x < y:
        return 0
    if x == y:
        return 1
    else:
        return F(x - 2, y) + F(x // 2, y)


print(F(28, 10) * F(10, 1))


def F(x, y):  # Trajectory: include 9, 11
    if x == y:
        return 1
    if x > y:
        return 0
    if x < y: 
        return F(x + 1, y) + F(x * 3, y) + F(x + 2, y)


print(F(2, 9) * F(9, 11) * F(11, 12))


def F(x, y):  # Trajectory: exclude 24
    if x == y: return 1

    if x > y or x == 24: return 0

    if x < y: return F(x + 1, y) + F(x * 2 + 1, y)


print(F(1, 25))


def F(x, y):
    if x == y: return 1

    if x > y: return 0

    if x < y: return F(x+3, y) + F(x*2, y)


print(F(1, 25))
