
def f(x):
    return (((x%a==0) and (x%45==0))<=(x%162==0))and(a>200)

for a in range(1,1000):
    if all(f(x)==1 for x in range(1,100000)):
        print(a)