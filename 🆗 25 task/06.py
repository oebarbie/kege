def divs(x):

    #перебор всех делителей
    #ds = {1, x}

    ds = set()
    for d in range(2, int(x**0.5)+1):
        if x % d == 0:
            ds.add(d)
            ds.add(x//d)
            #ds |= {d, x//d}
    return sorted(ds)

res = []
for x in range(500_001, 1_000_000):
    s = sum(divs(x))
    if s % 10 == 9:
        res.append(x)
        if len(res) == 5:
            break
for x in res:
    print(x, sum(divs(x)))
