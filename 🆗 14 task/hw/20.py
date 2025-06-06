def f(x, n):
    res = ''
    while x > 0:
        res = str(x%n) + res
        x //= n
    return res

n = 3*5**1984 - 7*25**777 - 11*125*666 - 404
print(f(n, 5).count('2'))
