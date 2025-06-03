from itertools import *

cnt = 0
for x in product('0123456', repeat=7):
    s = ''.join(x)
    if s[0] not in '035' and ('22' not in s or '44' not in s):
        cnt += 1
print(cnt)