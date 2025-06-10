from itertools import *

cnt = 0
for x in product(sorted('ТЕОРИЯ'), repeat=6):
    s = ''.join(x)
    cnt += 1
    if s[0] not in 'РТЯ' and s.count('И') >= 2 and cnt%2!=0:
        print(cnt, s)