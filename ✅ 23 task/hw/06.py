
def f(a,b):
    if a < b:
        return 0
    if a == b:
        return 1
    if a == 28:
        return 0
    if a % 2 == 0:
        return f(a//2, b) + f(a-2, b)
    else:
        return f(a-3, b) + f(a-2, b)

print(f(98, 1))