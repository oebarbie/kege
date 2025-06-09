
def f(n):
    cnt = 1
    if n >= 1:
        cnt += 1
        cnt += f(n-1)
        cnt += f(n-3)
        cnt += 1
    return cnt

print(f(40))