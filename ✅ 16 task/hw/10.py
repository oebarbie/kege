from fractions import Fraction
from functools import lru_cache

@lru_cache(None)
def f(n):
    if n < 20:
        return n
    if n >= 20:
        return (n-6)*f(n-7)

for i in range(1, 47858): f(i)

print((f(47872) - 290*f(47865))/f(47858))