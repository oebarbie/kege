from itertools import *

cnt = 0
for x in product('012345', repeat=6):
    s = ''.join(x)
    s = s.replace('3', '1').replace('5', '1')
    if s[0] != '0' and s.count('2') == 1 and '12' not in s  and '21' not in s:
        cnt += 1
print(cnt)