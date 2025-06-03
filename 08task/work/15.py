from itertools import *

i = 0
for x in product('ГЕКЭ023', repeat=4):
  i += 1
  s = ''.join(x)
  if s[0] in '023' and not('00' in s or '22' in s or '33' in s
                           or 'ГГ' in s or 'ЕЕ' in s or 'КК' in s or 'ЭЭ' in s):
    print(i)
    break