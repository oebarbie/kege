def divs(x):

    ds = set()
    for d in range(2, int(x**0.5)+1):
        if x%d == 0:
            ds.add(d)
            ds.add(x//d)
    return sorted(ds)


for x in range(224466, 664422):

    ds = divs(x)
    if ds:
        if ('5', '7', '13' in ds) and ('25', '49', '169' not in ds) and int(max(ds)) <= 100000 and int(max(ds)) % 100 == 19:
            print(x, max(ds))