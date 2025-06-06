def f(x, n):
    s = 0
    while x > 0:
        s += x%n
        x //= n
    return s

x = 43*7**103 - 21*7**57 + 98
print(f(x, 7))
