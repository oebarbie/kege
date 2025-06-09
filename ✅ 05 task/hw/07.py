def conv(x, n):
    res = ''
    while x>0:
        res = str(x%n) + res
        x //= n
    if res == '':
        return '0'
    return res

def f(n):
    x = str(conv(n, 3))
    if n % 3 == 0: x += x[-2:]
    else: x += conv(n%3*5, 3)

    return int(x, 3)

res = []
for x in range(133):
    if f(x) > 133:
        res.append(f(x))

print(min(res))