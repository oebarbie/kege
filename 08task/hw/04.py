from itertools import *

cnt = 0
for x in permutations('КАЛИЙ', r=5):
    s = ''.join(x)
    if s[0] != 'Й' and 'ИА' not in s:
        cnt += 1
print(cnt)