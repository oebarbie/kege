def tr(a,b,c):
    return a+b>c and a+c>b and b+c>a

def f(x):
    return tr(a,5,x)<=((max(x,11)<=19)==(not tr(23,13,x)))

for a in range(1,1000):
    if all(f(x)==1 for x in range(1,1000000)):
        print(a)