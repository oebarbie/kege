print('x y z w')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if ((z == (not x)) <= ((w <= (not y)) and (y <= x))) == 0:
                    print(y, z, x, w)