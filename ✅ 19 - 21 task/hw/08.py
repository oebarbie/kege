def f(s,m,end):
    if s>=end: return m%2==0
    if m==0: return 0
    h = [f(s+2,m-1,end),f(s*3,m-1,end)]
    return any(h) if m%2!=0 else all(h)

print(19, [end for end in range(16,1000) if f(15,2,end)])
print(20, [end for end in range(11,1000) if not f(10,1,end) and f(10,3,end)])
print(21, [end for end in range(6,1000) if not f(5,2,end) and f(5,4,end)])