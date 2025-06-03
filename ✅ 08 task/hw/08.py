from itertools import *

cnt = 0
for x in permutations('КОМЕТА'):
    s = ''.join(x)
    s = s.replace('А', 'О').replace('Е', 'О')
    s = s.replace('М', 'К').replace('Т', 'К')
    if not('ОО' in s or 'КК' in s):
        cnt += 1
print(cnt)