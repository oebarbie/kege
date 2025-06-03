from itertools import *

cnt = 0
for x in permutations('КОБУРА'):
    s = ''.join(x)
    s = s.replace('А', 'О').replace('У', 'О')
    s = s.replace('Б', 'К').replace('Р', 'К')
    if not('ОО' in s or 'КК' in s):
        cnt += 1
print(cnt)