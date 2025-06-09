def f(x):
    n = bin(x)[2:]
    n += n[-1]
    if n.count('1')%2 == 0:
        n += '0'
    else:
        n += '1'
    if n.count('1')%2 == 0:
        n += '0'
    else:
        n += '1'

    return int(n, 2)
    
for i in range(90):
    if f(i) > 90:
        print(i)
        break
    