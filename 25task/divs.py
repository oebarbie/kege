def divs(x):

    #перебор всех делителей
    #ds = {1, x}

    ds = set()
    for d in range(2, int(x**0.5)+1):
        if x % d == 0:
            ds.add(d)
            ds.add(x//d)
    return sorted(ds)
