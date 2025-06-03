from itertools import *

cnt = 0
for x in set(permutations('СОТОЧКА')):
    s = ''.join(x)
    if ('ОО' in s) or ('ОА' in s) or ('АО' in s):
        cnt += 1
print(cnt)

cnt = 0
for x in set(permutations('СОТОЧКА')):
    s = ''.join(x)
    s = s.replace('А', 'О')
    if 'ОО' in s:
        cnt += 1
print(cnt)