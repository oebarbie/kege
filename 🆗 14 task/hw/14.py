
for x in '0123456789ABCDE':
    n = int(f'1{x}51', 15) - int(f'3{x}2', 15)
    if n % 4 == 0:
        print(n//4)