from itertools import *

cnt = 0
for x in product('АВОРТ', repeat=4):
    cnt += 1
    s = ''.join(x)
    if s == 'ВАТА':
        print(cnt)
        break