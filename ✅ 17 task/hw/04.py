a = [int(x) for x in open('/home/me/kege/❌ 17 task/hw/04.txt')]

cnt = [x for x in a if x%52 == 0]
res = []

for x,y,z in zip(a, a[1:], a[2:]):
    if ((x%113)+(y%113)+(z%113)) == min(cnt):
        res.append(x+y+z)
print(len(res), max(res))