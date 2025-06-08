cnt = 0
for s in open('06.txt'):
    a = sorted([int(x) for x in s.split()])
    rep = [x for x in a if a.count(x)>1]
    nre = [x for x in a if a.count(x)==1]
    if len(rep)>0 and len(nre)>0:
            if (sum(nre)/len(nre)) < (sum(rep)/len(rep)):
                cnt += 1
print(cnt)
