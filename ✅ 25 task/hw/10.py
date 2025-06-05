from fnmatch import *

def divs(x):
    res = set()
    for d in range(2, int(x**0.5)+1):
        if x%d == 0:
            res.add(d)
            res.add(x//d)
    return res

for x in range(1, 10**6):

    ds = [d for d in divs(x) if fnmatch(str(d), '4*')]
    if len(ds) == 24:
        print(x, max(ds))