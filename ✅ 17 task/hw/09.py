from itertools import *

a = [int(x) for x in open('/home/me/kege/❌ 17 task/hw/09.txt')]

res = []

for x,y in combinations(a, 2):
    if (x+y)%120 == 0:
        res.append(x+y)
print(len(res), max(res))