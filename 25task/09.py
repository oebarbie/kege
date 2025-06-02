from fnmatch import *

def divs(x):
    ds = {1, x}
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            ds.add(i)
            ds.add(x//i)
    return sorted(ds)

for x in range(400_000, 500_001):
    s = str(x)
    cnt = 0
    cntn = 0
    ds = divs(x)
    for d in ds:
        if fnmatch(str(d), '*7?'):
            cnt += 1
            cntn += int(d)
    if cnt >= 18:
        print(x, cntn)
        cnt, cntn = 0, 0
    else:
        cnt, cntn = 0, 0