def f(n):
    x = bin(n)[2:]
    if x.count('1')%2 == 0:
        x += '0'
        x = '10' + x[2:]
    else:
        x += '1'
        x = '11' + x[2:]
    return int(x, 2)

for x in range(40):
    if f(x) > 40:
        print(x)
        break