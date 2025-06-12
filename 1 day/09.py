cnt = 0
for s in open('/home/me/kege/1 day/09.txt'):
    a = [int(x) for x in s.split()]
    cnt += 1

    rep = [x for x in a if a.count(x) == 2]
    nre = [x for x in a if a.count(x) == 1]
    
    if len(rep) == 4 and len(nre) == 3:
        if (sum(rep)/len(rep)) < max(nre):
            print(cnt, rep, nre)

