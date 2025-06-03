from itertools import *

cnt = 0
for x in product('0123456', repeat = 5):
    s = ''.join(x)
    ch, nch = 0, 0
    if s[0] != '0' and s.count('6') == 1:
        nch = [c for c in s if c in '135']
        ch = [c for c in s if c in '0246']
        if sum(map(int, ch)) < sum(map(int, nch)):
            cnt += 1

        # for d in s:
        #     if int(d)%2 == 0: ch += int(d)
        #     else: nch += int(d)
        # if ch <= nch:
        
print(cnt)