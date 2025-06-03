from itertools import *

#чиса на 0 не начинаются!!!!

cnt = 0
for x in product('01234', repeat = 6):
    s = ''.join(x)
    if s[-1] != '3' and s[-1] != '4' and s[0] != '1' and s[0] != '0':
        cnt += 1
print(cnt)