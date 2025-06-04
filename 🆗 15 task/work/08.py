def f(x):
    return ((x&8375!=0) or (x&6743!=0))<=(x&a>0)

for a in range(1,100000):
    if all(f(x)==1 for x in range(0,10000000)):
        print(a)