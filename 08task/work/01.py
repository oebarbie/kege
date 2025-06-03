from itertools import *

# проверить, что числа не повторяются ->
# проверить длину set

cnt = 0
for x in product('0123456789', repeat=6):
    s = ''.join(x)
    if s[0] != '0' and len(set(s)) == 6:
        for c in '2468': s = s.replace(c, '0')
        for c in '3567': s = s.replace(c, '1')
        if not('00' in s or '11' in s):
        #if '00' not in s and '11' not in s:
            cnt += 1
print(cnt)

k = 0
for x in product('0123456789', repeat=6):
  s = ''.join(x)
  if s[0] != '0' and len(set(s)) == 6:
    for c in '2468': s = s.replace(c, '0')
    for c in '3579': s = s.replace(c, '1')
    #  не (условие на строку, которая не подходит)
    if not('00' in s or '11' in s):
      k += 1
print(k)


