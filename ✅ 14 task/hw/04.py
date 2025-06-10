
def f(x):
    s = 0
    while x > 0:
        s += x%4
        x //= 4
    return s

res = set()
for x in range(0, 1_000_000):
    n = 3*16**2018 - 2*8**1028 - 3*4**1100 - 4**x - 2022
    if n < 0:
        break
    S = f(n)
    res.add(S)

print(len(set(res)))