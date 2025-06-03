from itertools import *

cnt = 0 
for x in product(sorted('КОМПЬЮТЕР'), repeat = 5):
    cnt += 1
    s = ''.join(x)
    if s[0] != 'Ь' and s.count('К') == 2:
        print(cnt)