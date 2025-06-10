
def f(x):
    s = 0
    i = len(x) - 1
    for d in x:
        s += d*37**i
        i -= 1
    return s

for x in range(37):
    a = f([12, 5, 9, x, 11, 10, 9, 8, 15])
    b = f([14, 3, x, 5, 13, 10, 9, 12, 6])

    if (a*b) % 36 == 0:
        print(f([2, x, 1]))
