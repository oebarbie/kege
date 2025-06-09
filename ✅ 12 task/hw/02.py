s = '>' + '1'*28 + '2'*18 + '3'* 35

while '>1' in s or '>2' in s or '>3' in s:
    if '>1' in s:
        s = s.replace('>1', '22>', 1)
    if '>2' in s:
        s = s.replace('>2', '2>1', 1)
    if '>3' in s:
        s = s.replace('>3', '1>2', 1)

print(sum(int(x) for x in s if x != '>'))

print(4*28 + 6*18 + 7*35)
# руками