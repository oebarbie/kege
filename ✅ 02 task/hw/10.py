print('x y z w')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if (w and ((z or y) == (z and x))) == 1:
                    print(x, y, z, w)