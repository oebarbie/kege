def f(s, m):
    if s == 0: return m%2 == 0
    if m == 0: return 0
    h = [f(s-1,m-1)]
    if (s-2) >= 0: h.append(f(s-2,m-1))
    if (s-4) >= 0: h.append(f(s-4,m-1))

    return any(h) if m%2!=0 else all(h)

print(19, [s for s in range(1, 16) if f(s,2)]) #any
print(20, [s for s in range(1, 16) if not f(s,3) and f(s,5)])
print(21, [s for s in range(1, 16) if f(s,20)])
