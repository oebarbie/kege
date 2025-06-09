def conv(x, n):
    res = ''
    while x > 0:
        res = str(x%n) + res
        x //= n
    return res

def f(n):
    x = conv(n, 7)
    if x.count('2') % 2 == 0:
        x += '555'
    else:
        x = '1' + x

    return int(x, 7)

for x in range(3799, -1, -1):
    if f(x) < 3799:
        print(x)
        break