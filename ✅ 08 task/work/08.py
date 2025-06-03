from itertools import *

# for a1 in 'РОСОМАХА':
#     for a2 in 'РОСОМАХА':
#         for a3 in 'РОСОМАХА':
#             for a4 in 'РОСОМАХА':
#                 for a5 in 'РОСОМАХА':
#                     for a6 in 'РОСОМАХА':
#                         for a7 in 'РОСОМАХА':
#                             for a8 in 'РОСОМАХА':

cnt = 0
for x in set(permutations('РОСОМАХА')):
    s = ''.join(x)
    s = s.replace('А', 'О')
    s = s.replace('С', 'Р')
    s = s.replace('М', 'Р')
    s = s.replace('Х', 'Р')
    if 'ОО' not in s and 'РР' not in s:
        cnt += 1
print(cnt)


