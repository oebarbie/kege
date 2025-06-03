from itertools import *

cnt = 0 
for x in product(sorted('ФЕВРАЛЬ'), repeat = 6):
    cnt += 1
    s = ''.join(x)
    s = s.replace('Е', 'А')
    if 'А' not in s:
        print(cnt)
        break