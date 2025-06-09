def f(n):
    x = bin(n)[2:]
    cnt = sum([int(d) for d in x])
    if cnt%2 != 0:
        x += '11'
    else:
        x = '11' + x
    a = int(x, 2)
    return a

for x in range(500):
    if f(x) > 102:
        print(x)
        break
