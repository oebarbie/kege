from fractions import Fraction
from functools import lru_cache

@lru_cache(None)
def f(n):
    if n >= 10_000:
        return Fraction(1)
    if n < 10_000 and n%2 == 0:
        return f(n+1)*f(n+2)
    if n < 10_000 and n%2 != 0:
        return (n+2)/f(n+2)
    
for i in range(10_000, 9, -1): f(i)
print(f(10)/f(38))