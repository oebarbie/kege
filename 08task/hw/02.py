from itertools import *

cnt = 0
for x in product('ABCDX', repeat=4):
    s = ''.join(x)
    if s.count('X')==1:
        cnt += 1
print(cnt)