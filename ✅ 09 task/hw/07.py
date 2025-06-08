cnt = 0
k = 0

for s in open('07.txt'):
    a = sorted([int(x) for x in s.split()])
    rep = [x for x in a if a.count(x) == 2]
    nre = [x for x in a if a.count(x) == 1]

    if len(rep) == 4 and len(nre) == 3:
        if (sum(rep)/len(rep)) < (sum(a)/len(a)):
            cnt += 1
print(cnt)
