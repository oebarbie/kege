from itertools import *

cnt = 0
for x in combinations('FEDCBA9876543210', repeat=15):
    s = ''.join(x)
    for x in '02468ACE': s = s.replace(x, '0')
    for x in '13579BDF': s = s.replace(x, '1')
    if not ('00' in s or '11' in s):
        cnt += 1
print(cnt)