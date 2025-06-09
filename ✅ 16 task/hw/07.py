from functools import lru_cache

@lru_cache(None)
def f(n):
    if n > 3000:
        return n
    if n <= 3000:
        return (2*n + 4)*f(n+2)

for i in range(3000, 19, -1): f(i)

print(f(20)/f(28))