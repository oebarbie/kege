# два знака = 10(n) <= X < 100(n)
# три знака = 100(n) <= X < 1000(n)

# for x in range(2, 1000):
#     if int('10', x) <= 50 < int('100', x):
#         print(x)
#         break

def conv(x, n):
    res = []
    while x > 0:
        res = [x%n] + res
        x //= n 
    return res

for n in range(1, 30):
    x = conv(50, n)
    if len(x) == 2:
        print(n)
    