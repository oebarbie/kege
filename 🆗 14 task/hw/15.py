

for x in '0123456789ABCDE':
    for y in '0123456789ABCDEFG':
        n = int(f'123{x}5', 15) + int(f'67{y}9', 17)
        if n % 131 == 0:
            print(x, y, n//131)