from itertools import *

cnt = 0
for x in set(permutations('АМФИБРАХИЙ')):
    s = ''.join(x)
    if s[0:2] == 'АМ' and s[8:10] == 'ИЙ':
        cnt += 1
print(cnt)

cnt = 0
for x in permutations('ФИБРАХ', r = 6):
    cnt += 1
print(cnt)