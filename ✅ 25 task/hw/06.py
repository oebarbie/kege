def divs(x):

    ds = set()
    for d in range(2, int(x**0.5)+1):
        if x%d == 0:
            ds.add(d)
            ds.add(x//d)
    return sorted(ds)


for x in range(224466, 664423):

    ds = divs(x)
    if len(ds) > 0 and ds[-1] < 100000 and ds[-1] % 100 == 19:
        if all(x%d == 0 and x%(d**2) != 0 for d in (5,7,13)):
            print(x, ds[-1])