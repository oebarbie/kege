
def f(n):
    n1, n2, n3, n4 = n//1000, n%1000//100, n%100//10, n%10
    cnt = sorted([n1*n2, n1*n3, n1*n4])
    x = str(cnt[-2]) + str(cnt[-1])
    return x

for x in range(10000):
    if f(x) == '5472':
        print(x)
        break