from itertools import *

a = [int(x) for x in open('/home/me/kege/❌ 17 task/hw/10.txt')]

res = []

for x,y in combinations(a, 2):
    if (abs(x-y)%36==0) and (x%13==0 or y%13==0):
        res.append(abs(x-y))
print(len(res), max(res))
