a = [int(x) for x in open('/home/me/kege/❌ 17 task/hw/02.txt')]
mn = min(a)
res = []
for x,y in zip(a, a[1:]):
    if x%43==mn and y%43==mn:
        res.append(abs(x-y))
print(len(res), max(res))