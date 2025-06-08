cnt = 0
k = 0
for s in open('05.txt'):
    a = sorted([int(x) for x in s.split()])
    a1 = sorted([a[x] for x in range(1, len(a)) if a[x-1] == a[x]])
    a2 = [x for x in a if x not in a1]
    if len(set(a)) == 4 and len(set(a1)) == 2 and len(set(a2)) == 2:
        if (a1[-1])**2 > a2[0]*a2[1]:
            cnt += 1
print(cnt)
