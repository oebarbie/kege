for s in open('09.txt'):
    a = [int(x) for x in s.split()]
    rep = [x for x in a if a.count(x) == 2]
    nre = [x for x in a if a.count(x) == 1]

    if len(rep) == 4 and len(nre) == 3:
        if max(a) not in rep:
            print(sum(a))
            break
