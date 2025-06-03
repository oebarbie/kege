from itertools import *

cnt = 0
for x in product('0123456789ABCDEF', repeat=5):
    s = ''.join(x)
    if s[0] not in '01' and s[4] not in '02468ACE':
        cnt += 1
print(cnt)