def f(n):
    x = bin(n)[2:]
    res = ''
    for d in x:
        if d == '1': res += '0'
        else: res += '1'
    res = '1' + res

    if res.count('1')%2 == 0:
        res += '0'
    else:
        res += '1'
    return int(res, 2)

for x in range(180):
    if f(x) > 180:
        print(x)
        break