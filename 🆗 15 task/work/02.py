
def f(x):
    return (a%12==0)and(530%x==0)<=((not(a%x==0))<=(not(170%x==0)))

for a in range(1, 1001):
    if all(f(x) == 1 for x in range(1, 10000000)):
        print(a)