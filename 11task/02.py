from math import *

bit = ceil(log2(10+52+963))

for p in range(100000, 1, -1):

    pas = ceil(p*bit/8)
    
    if (2000*pas <= 693*1024):
        print(p)
        break