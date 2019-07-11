from math import factorial


def comb(n, k):
    return factorial(n) / (factorial(n-k) * factorial(k))


def p(k):
    s = 0.0
    for i in range(100 - k + 1):
        s += comb(100, i)
    return s / (2 ** 100)


def dice(k):
    return comb(10, k) * (1 / 6)**k * (5 / 6)**(10-k)


for i in [57, 58, 59, 60]:
    print(p(i))
