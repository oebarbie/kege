from itertools import *

cnt = 0
for x in product('012345678', repeat = 7):
    s = ''.join(x)
    if s[0] not in '037':
        if '00' not in s and '11' not in s and '22' not in s and \
        '33' not in s and '44' not in s and '55' not in s and \
        '66' not in s and '77' not in s and '88' not in s:
            cnt += 1
        # if all(c*2 not in s for c in '012345678')
print(cnt)