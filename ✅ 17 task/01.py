a = [int(x) for x in open('17/01.txt')]

for x,y in zip(a,a[1:]):
    x == y 

# для отрицательных чисел проверка последних чисел:
# abs(x)%10 == 3 - окончание числа
# str(x)[-1] == '3'
# для отриц чисел по модулю

for i in range(len(a)-1):
    x, y = a[i], a[i+1]

# перебор троек
for x,y,z in zip(a,a[1:],a[2:]):
    x = y

for i in range(len(2)-2):
    x,y,z= a[i],a[i+1],a[i+2]