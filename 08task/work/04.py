cnt = 0

for a1 in 'НИЧЯ':
    for a2 in 'НИЧЬЯ':
        for a3 in 'НИЧЬЯ':
            for a4 in 'НИЧЬЯ':
                for a5 in 'НИЧЬЯ':
                    s = a1+a2+a3+a4+a5
                    if 'ЬИЯ' not in s:
                        # if len(set(s)) == 5: (так как в set все символы уникальные)
                        if s.count('Н') == 1 and s.count('И') == 1 and s.count('Ч') == 1:
                            if s.count('Ь') == 1 and s.count('Я') == 1:
                                cnt += 1
print(cnt)


from itertools import *

cnt = 0
for x in permutations('ничья', r=5):
    s = ''.join(x)
    if s[0] != 'ь' and 'ьия' not in s:
        cnt += 1
print(cnt)
