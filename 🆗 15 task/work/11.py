def f(x):
    P = 20<=x<=50
    Q = 10<=x<=60
    A = a1<=x<=a2
    return (P<=A)and(A<=Q)

ox = [dx for x in (20,50,10,60) for dx in (x,x+0.01,x-0.01)]

m = []
for a1 in ox:
    for a2 in ox:
        if a2>a1 and all(f(x)==1 for x in ox):
            m.append(a2-a1)
print(max(m))