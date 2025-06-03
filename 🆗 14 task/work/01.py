# bin, oct, hex
# bin(10) = '0x1010'
# oct(10) = '0o12'
# hex(10) = '0xa'
# int(str, base)

x = 8**2014 - 2**614 + 45
print(bin(x)[2:].count('1'))