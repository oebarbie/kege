from itertools import *

cnt = 0
for x in product('ЛЕТО', repeat=4):
    s = ''.join(x)
    if s.count('Е')>=1:
        cnt += 1
print(cnt)