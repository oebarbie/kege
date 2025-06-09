def f(n):
    x = bin(n)[2:]
    if n%3 == 0:
        x += x[-3:]
    else:
        x += bin(n%3*3)[2:]
    return int(x, 2)

res = set()
for x in range(8, 151):
    if f(x) > 151:
        res.add(f(x))
        break
print(min(res))