from math import *

for i in range(1, 10000):

    bit = ceil(log2(i))
    pas = ceil(bit*1231/8)

    if (pas*523872 > 432*1024**2):
        print(i)
        break