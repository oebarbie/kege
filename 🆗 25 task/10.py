def divs(x):
    ds = set()

    for d in range(2, int(x*0.5)+1):
        if x % d == 0:
            ds.add(d)
            ds.add(x//d)

    return sorted(ds)

for x in range(326496, 649633):
    ds = divs(x)

    ev = [d for d in ds if d % 2 == 0]
    od = [d for d in ds if d % 2 != 0]

    if len(od) == len(ev) and len(od) >= 70:
        print(x, min(d for d in ds if d > 1000))
