from itertools import *

cnt = 0
for x in set(permutations('ПРОСТО')):
    s = ''.join(x)
    if 'ОО' not in s:
        cnt += 1
print(cnt)