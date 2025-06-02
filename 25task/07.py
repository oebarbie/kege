def divs(x):

    #перебор всех делителей
    #ds = {1, x}

    ds = {1}
    for d in range(2, int(x**0.5)+1):
        if x % d == 0:
            ds.add(d)
            ds.add(x//d)
    return sorted(ds)


cnt = 5
for x in range(770_000-1, -1, -1):
    ds = divs(x)
    av = sum(ds) // len(ds)
    if cnt != 0:
        if av % 100 == 12:
            print(x, av)
            cnt -= 1

