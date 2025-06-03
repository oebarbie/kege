from itertools import *

cnt = 0
for x in product('СПОЛКЙЕДА', repeat=6):
    s = ''.join(x)
    if s[0] == 'К' and s.count('Й') >= 2 and s.count('С') == 0 and s.count('Е') == 0 and cnt % 2 == 0:
        print(cnt)
        break
    cnt += 1
        
