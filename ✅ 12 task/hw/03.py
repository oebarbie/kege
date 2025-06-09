cnt = 0
for i in range(1, 101):
    s = '1' + '0'*i

    while '10' in s or '1' in s:
        if '10' in s:
            s = s.replace('10', '0001', 1)
        else:
            if '1' in s:
                s = s.replace('1', '0', 1)

    if len(s) % 7 == 0:
        cnt += 1

print(cnt)