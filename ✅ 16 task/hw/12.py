def f(n):
    cnt = n+1
    if n > 1:
        cnt += n+5
        cnt += f(n-1)
        cnt += f(n-2)
    return cnt

print(f(30))