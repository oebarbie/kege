print('a b c t')
for a in 0,1:
    for b in 0,1:
        for c in 0,1:
            for t in 0,1:
                if ((not a or not b) and (c <= (not a)) and (t and not a or c and not b)) == 0:
                    print(a, b, c, t)