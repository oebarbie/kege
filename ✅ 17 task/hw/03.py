a = [int(x) for x in open('/home/me/kege/❌ 17 task/hw/03.txt')]

cnt = [x for x in a if x%32==0]
res = []

for x,y in zip(a, a[1:]):
    if (x<0 or y<0) and ((x+y) < len(cnt)):
        res.append(x+y)
print(len(res), max(res))