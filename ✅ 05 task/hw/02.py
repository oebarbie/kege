def f(n):
    x = bin(n)[2:]
    if n % 2 != 0: 
        x += '0'
    else: 
        x = '1' + x
    if x.count('1') % 2 == 0:
        x += '1'
    else:
        x += '0'
    return int(x, 2)

for x in range(228):
    if f(x) > 228:
        print(x)
        break