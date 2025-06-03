from itertools import *

cnt = 0
for x in set(permutations('АМФИБРАХИЙ')):
    s = ''.join(x)
    if 'ИИФАА' in s or 'ААФИИ' in s:
        cnt += 1
print(cnt) 