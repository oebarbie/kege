
def divs(x):

    res = set()
    for d in range(2, int(x*0.5)+1):
        if x%d == 0:
            res.add(d)
            res.add(x//d)
    return sorted(res)

cnt = 0
for x in range(1_125_000, 10_125_000):
    ds = divs(x)
    d7 = [d for d in ds if d != 7 and d % 10 == 7]
    if len(d7) > 0 and cnt < 5:
        print(x, d7[0])
        cnt+=1