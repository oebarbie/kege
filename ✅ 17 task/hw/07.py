a = [int(x) for x in open('/home/me/kege/❌ 17 task/hw/07.txt')]

cnt = [x for x in a if abs(x)%1000 == 121]
res = []

def check(x):
    if 1000 <= abs(x) <= 9999 and x%2 == 0:
        return 1
    else:
        return 0

for x,y,z in zip(a, a[1:], a[2:]):
    if check(x)+check(y)+check(z) <= 1:
        if (x+y+z) <= max(cnt):
            res.append(x+y+z)
print(len(res), max(res))