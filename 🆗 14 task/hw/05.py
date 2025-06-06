from string import printable

def conv(x, n):
    res = ''
    while x > 0:
        res = str(printable[x%n]) + res
        x //= n
    return res

for n in range(2, 1_000_00):
    x = conv(70, n)
    if len(x) == 3:
        print(n)
        break