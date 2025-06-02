from itertools import *

st = []
for i in range(5):
    st += [''.join(c) for c in product('0123456789', repeat=i)]

res = set()
for a in st:
    for b in st:
        if len(a) + len(b) > 4:
            break
        x = int('4' + a + '4736' + b + '1')
        if x % 7993 == 0:
            res.add(x)

for x in sorted(res):
    print(x, x // 7993)