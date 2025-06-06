def conv(x, n):
    res = ''
    while x > 0:
        res = str(x%n) + res
        x //= n
    return res

for x in range(2030, -1, -1):
    n = 3**100 - x
    if conv(n, 3).count('0') == 1:
        print(x)
        break