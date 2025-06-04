def ug(a,b,c):
    return a+b+c==180

def f(x):
    return ug(37,a,x+45) == (ug(a,x,90) and not(a+23<120))

for a in range(1,1000):
    if all(f(x)==1 for x in range(1,1000000)):
        print(a)