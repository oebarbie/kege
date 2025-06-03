
cnt = 0 
for a1 in 'КАТЕР':
    for a2 in 'КАТЕР':
        for a3 in 'КАТЕР':
            s = a1+a2+a3
            if s.count('Р') >= 2:
                cnt += 1
print(cnt)

