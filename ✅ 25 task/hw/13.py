# from fnmatch import *

# def divs(x):
#     res = set()
#     for d in range(2, int(x**0.5)+1):
#         if x%d == 0:
#             res |= {d, x//d}
#     return res

# for x in range(10**6, 10**10+1):
#     if len(divs(x)) == 1:
#         if fnmatch(str(x), '1?2*0*2?1'):
#             print(x)

from fnmatch import fnmatch

def divs(x):
  ds = set()
  for d in range(2, int(x**.5)+1):
    if x % d == 0:
      ds |= {d, x//d}
  return sorted(ds)

for sq in range(10**5):
  x = sq**2
  if fnmatch(str(x), '1?2*0*2?1'):
    if len(divs(sq)) == 0:
      print(x)