from itertools import *

cnt = 0
for x in product('01234', repeat=6):
    s = ''.join(x)
    if int(s, 5) % 2 == 0 and s[0] == '3' :
        cnt += 1
print(cnt)