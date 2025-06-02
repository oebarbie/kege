from fnmatch import *

for x in range(0, 10**8):
    if fnmatch(str(x), '*15*7424'):

        if x % 111 == 0:
            print(x, x//111)
        elif x % 113 == 0:
            print(x, x//113)
        elif x % 127 == 0:
            print(x, x//127)