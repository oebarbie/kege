# from string import printable

# def conv(x, n):
#     res = ''
#     while x > 0:
#         res = str(printable[x%n]) + res
#         x //= n
#     return res

# for n in range(1, 36):
#     if conv(41, n) % 10 == 2 and conv(131, n) % 10 == 1:
#         print(n)

# print(conv(41, 3))

for n in range(2, 37):
  if 41 % n == 2 and 131 % n == 1:
    print(n)