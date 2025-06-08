cnt = 0
for s in open('01.txt'):
    a = sorted([int(x) for x in s.split()])
    if a[2]**2 > 2*a[1]*a[0]:
        cnt += 1
print(cnt)
