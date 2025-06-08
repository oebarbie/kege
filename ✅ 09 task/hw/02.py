cnt = 0
for s in open('02.txt'):
    a = sorted([int(x) for x in s.split()])
    if ((a[0] + a[3])**2) > (a[1]**2 + a[2]**2):
        cnt += 1
print(cnt)
