from itertools import *

cnt = 0
for x in product('АВСХ', repeat=5):
    s = ''.join(x)
    if (s.count('Х')==1 and s[4]=='Х') or s.count('Х')==0:
        cnt += 1
print(cnt)