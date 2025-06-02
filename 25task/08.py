def divs(x):
    ds = set()
    for d in range(2, int(x**0.5)+1):
        if x%d == 0:
            ds.add(d)
            ds.add(x//d)
    return sorted(ds)

cnt = 5
for i in range(800_001, 1_000_000):
    ds = divs(i)    

    if ds:
        m = max(ds) + min(ds)
    else:
        m = 0

    if cnt != 0:
        if m % 10 == 4:
            print(i, m)
            cnt -= 1
