a = [int(x) for x in open('/home/me/kege/❌ 17 task/hw/05.txt')]

cnt = [x for x in a if abs(x)%10 == 9]
res = []

for x,y  in zip(a, a[1:]):
    if (abs(x)%10==9 and abs(y)%10!=9) or (abs(x)%10!=9 and abs(y)%10==9):
        if (x**2 + y**2) < max(cnt)**2:
            res.append(x**2 + y**2)
print(len(res), min(res))