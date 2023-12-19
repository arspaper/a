def getBase(num, base):
    snum = str(num)
    degree = 0
    sum = 0
    for digit in snum[::-1]:
        sum += int(digit) * (base ** degree)
        degree += 1
    return sum


og = 110
tgt = 39800

for i in range(2, 100000):
    num = getBase(og, i)
    if num == tgt:
        print(i)
        break
