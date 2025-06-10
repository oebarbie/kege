def f(s, m, t):
    if s >= 21: return m%2 == 0
    if m == 0: return 0
    h = []
    if t[-2]!='1': h.append(f(s+1, m-1, t+'1'))
    if t[-2]!='2': h.append(f(s+2, m-1, t+'2'))
    if t[-2]!='3': h.append(f(s*2, m-1, t+'3'))
    return any(h) if m%2!= 0 else all(h)

print(19, [s for s in range(1, 21) if not f(s, 1, '00') and f(s, 3, '00')])
print(20, [s for s in range(1, 21) if not f(s, 2, '00') and f(s, 4, '00')])
print(21, [s for s in range(1, 21) if not f(s, 1, '00') and not f(s, 3, '00') and f(s, 5, '00')])