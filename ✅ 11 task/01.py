from math import *

for kod in range(1000000,1,-1):
    bit = ceil(log2(kod))
    nom = ceil(71_118*bit/8)
    if 12_288*nom <= 2*1024**3:
        print(kod)
        break