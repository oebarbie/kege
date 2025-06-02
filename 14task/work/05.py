
def con(x, n):
    res = []
    while x > 0:
        res = [x%n] + res
        x //= n
    return res

for n in range(1, 50):
    x = con(68, n)
    if x % 10 == 2 and len(x) == 4:
        print(n)