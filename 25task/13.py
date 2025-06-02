# def divs(x):
#     ch = set()
#     for d in range(2, int(x**0.5)+1):
#         if x%d == 0 and d%2==0:
#             ch.add(d)
#         if (x//d) % 2 == 0:
#             ch.add(x//d)
#     return(ch)

# print(divs(9))

def divs(x):
    ds = {1, x}
    for d in range(2, int(x**0.5)+1):
        if x % d == 0:
            ds.add(d)
            ds.add(x//d)
    return sorted(ds)

cnt = 5
for k in range(1, 1_000_000):
    s = 1_850_000_000 + k
    ds = divs(s)
    
    ch = set()
    for d in ds:
        if d % 2 == 0:
            ch.add(d)

    if len(ch) % 2 != 0:
        if cnt != 0:
            print(k, len(ch))
            cnt -= 1