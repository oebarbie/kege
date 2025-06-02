from itertools import *

cnt = 0
sum = 0

for i in range(7):
    for s in product('0123456789', repeat = i):
        a = ''.join(s)
        for b in range(10):
            x = int(f'1{a}28{b}64')
            if x % 596 == 0:
                cnt += 1
                sum += x

print(cnt, sum//cnt)