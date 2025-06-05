from fnmatch import *

for x in range(0, 10**9, 21):
    s = str(x)
    if fnmatch(s, '1*5*9'):
        if all(a < b for a, b in zip(s, s[1:])):
            print(x, x//21)