def f(a, b, m):
    if (a+b) >= 231: return m%2 == 0
    if m == 0: return 0
    h = [f(a+1, b, m-1), f(a, b+1, m-1), f(a*2, b, m-1), f(a, b*2, m-1),]
    return any(h) if m%2 != 0 else all(h)

print(19, [b for b in range(1, 214) if f(17, b, 2)]) # any
print(20, [b for b in range(1, 214) if not f(17, b, 1) and f(17, b, 3)])
print(21, [b for b in range(1, 214) if not f(17, b, 2) and f(17, b, 4)])