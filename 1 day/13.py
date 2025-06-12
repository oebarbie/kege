# cnt = 0
# for x in 0,1:
#     for y in 0,1:
#         for z in 0,1:
#             for w in 0,1:
#                 if (x+y+z+w)%2 == 0:
#                     cnt += 1
# print(cnt)


from itertools import *

cnt = 0
for x in product('01', repeat=20):
    s = ''.join(x)
    if s.count('1') %3 != 0:
        cnt += 1
print(cnt)