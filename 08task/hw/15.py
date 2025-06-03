from itertools import *

cnt = 0
for x in product('АБЕЁЗР', repeat=6):
    cnt += 1
    s = ''.join(x)
    if s == 'РАЗРАБ':
        print(cnt)
        break