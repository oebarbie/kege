from fnmatch import *

for x in range(0, 10**10, 2025):
    s = str(x)
    if fnmatch(s, '33?2*42?') and fnmatch(s, '*32??2?'):
        print(x, x//2025)