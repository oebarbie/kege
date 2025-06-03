from itertools import *

cnt = 0
for x in product('01234567', repeat=4):
    s = ''.join(x)
    if s[0] in '246':
        if s[0] >= s[1] and s[1] >= s[2] and s[2] >= s[3]:
            cnt += 1
print(cnt)