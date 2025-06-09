# каширование

from functools import lru_cache

@lru_cache(None)
def f(n):
    return n   
for i in range(1, 8765, 1): f(i)

# для норм деления
from fractions import Fraction