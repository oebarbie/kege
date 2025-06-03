cnt = 0

for a1 in 'ШКОЛА':
    for a2 in 'ШКОЛА':
        for a3 in 'ШКОЛА':
             s = a1+a2+a3
             if s.count('К') == 1:
                 cnt += 1
print(cnt)


from itertools import *

cnt = 0 
for x in product('ШКОЛА', repeat=3):
    if x.count('К') == 1:
        cnt += 1
print(cnt)