res = []

for n in range(100, 1_000):

    s = '5'*n

    while '555' in s or '11' in s or '2' in s:
        if '555' in s:
            s = s.replace('555', '1', 1)
        if '11' in s:
            s = s.replace('11', '25', 1)
        if '2' in s:
            s = s.replace('2', '5', 1)

    # макс R = 155
    if n > 100 and n % 9 == 0 and s =='155':
        res.append(n)

print(min(res)) # 155