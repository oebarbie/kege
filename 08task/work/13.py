from itertools import *

cnt = 0 
for x in product(sorted('МАРИЯ'), repeat = 4):
    cnt += 1
    s = ''.join(x)
    if s == 'АРИЯ':
        print(cnt)
        break