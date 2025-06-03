from itertools import *

cnt = 0
for x in product(sorted('ПАРУС'), repeat=5):
    cnt += 1
    s = ''.join(x)
    if s[0] == 'У' and 'АА' not in s:
        print(cnt)
        break