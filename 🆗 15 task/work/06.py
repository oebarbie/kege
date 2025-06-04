def f(x,y):
    return (5*x-6*y<a) or (x-y>30)

for a in range(0,1000):
    if all(f(x,y)==1 for x in range(0,1000) for y in range(0,1000)):
        print(a)