a = [int(x) for x in open('/home/me/kege/❌ 17 task/hw/01.txt')]

res = []
for x,y in zip(a,a[1:]):
    if (abs(x)%7==0 or abs(y)%7==0) and (abs(x)%10==3 or abs(y)%10==3):
        res.append(x+y)
print(len(res), min(res))