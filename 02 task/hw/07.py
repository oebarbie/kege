print('w x y z')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if (not(y <= (x==w)) and (z <= x)) == 1:
                    print(w, x, y, z)