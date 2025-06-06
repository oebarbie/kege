def f(x, n):
    res = ''
    while x > 0:
        res = str(x%n) + res
        x //= n
    return res

n = 7**202 + 49**102 - 7**20
x = f(n, 7)
print(str(x).count('6'))