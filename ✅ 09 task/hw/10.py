cnt = 0
for s in open('10.txt'):
    a = [int(x) for x in s.split()]
    rep = [x for x in a if a.count(x) == 2]
    nre = [x for x in a if a.count(x) == 1]
    cnt += 1
    if len(rep) == 2 and len(nre) == 4:
        if rep[0] >= (sum(nre)/len(nre)):
            print(cnt)
            break
        
