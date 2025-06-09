from functools import lru_cache

@lru_cache(None)
def f(n):
    if n == 1:
        return 3
    if n > 1 and n % 2 == 0:
        return f(n-1)+5*(n-1)
    if n > 1 and n % 2 != 0:
        return f(n-1) + 7
    
for i in range(1, 8765, 1): f(i)
    
print(f(8765))
