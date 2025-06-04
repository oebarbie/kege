def f(x):
    return (160<=x<=180)<=((x%35==0)<=(x%a==0))

for a in range(1,1000):
    if all(f(x)==1 for x in range(1,100000)):
        print(a)