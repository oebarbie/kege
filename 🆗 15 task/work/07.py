def f(x,y):
    return (5*x+y>63) or (x>2*y) or (3*x+2*y<a)

for a in range(1,1000):
    if any(f(x,y)==0 for x in range(0,1000) for y in range(0,1000)):
        print(a)