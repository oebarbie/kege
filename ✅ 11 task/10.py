from math import *

for i in range(1000000, -1, -1):

    bit = ceil(log2(8200))
    pas = ceil(bit*303/8)
    pas += i

    if (101*pas <= 101*1024):
        print(i)
        break
    