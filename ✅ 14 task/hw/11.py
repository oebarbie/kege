from string import printable

def conv(x, n):
    s = 0
    while x>0:
        s += x%n
        x //= n
    return s

for x in range(1, 1_000):
    n = 36**17 - 6**x + 71
    if conv(n, 6) == 61:
        print(x)
        break
