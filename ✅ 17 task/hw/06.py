a = [int(x) for x in open('/home/me/kege/❌ 17 task/hw/06.txt')]

cnt = [x for x in a if x % 100 == 13]
res = []

for x,y,z in zip(a, a[1:], a[2:]):
    if (100 <= x <= 999 and 100 <= y <= 999 and not(100 <= z <= 999)) or \
       (100 <= x <= 999 and 100 <= z <= 999 and not(100 <= y <= 999)) or \
       (100 <= z <= 999 and 100 <= y <= 999 and not(100 <= x <= 999)):
       if (x+y+z) <= max(cnt):
           res.append(x+y+z)
print(len(res), max(res))