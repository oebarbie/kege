a = [int(x) for x in open('/home/me/kege/❌ 17 task/hw/08.txt')]

cnt = [x for x in a if 100<=abs(x)<=999 and abs(x)%100 == 15]
res = []

def ch(x):
    if x>=0: return 1
    else: return 0

for x,y,z in zip(a, a[1:], a[2:]):
    if ((ch(x)+ch(y)+ch(z)) == 3) or ((ch(x)+ch(y)+ch(z)) == 0):
        if min(x,y,z)*max(x,y,z) > min(cnt)**2:
            res.append(min(x,y,z)*max(x,y,z))
print(len(res), min(res))