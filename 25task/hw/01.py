from fnmatch import *

for d in range(0, 10**12+1, 98591):

    if fnmatch(str(d), "12?3*456??9"):
        print(d, d // 98591)