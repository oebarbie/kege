from math import *

for i in range(100000, 1, -1):

    bit = ceil(log2(i))
    pas = ceil(23*bit/8)

    if (500_000*pas <= 21*1024**2):
        print(i)
        break