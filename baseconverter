def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    a = ""
    for element in digits[::-1]:
        a += str(element)
    return a
