# def f(x, n):
#     res = ''
#     s = 0
#     while x > 0:
#         res = str(x%n) + res
#         s += x%n
#         x //= n
#     return res, s

# for x in range(1_000_0000000000, 0, -1):
#     n = 7**500 + 7**200 - 7**50 - x
#     n, s = f(n, 7)
#     if int(n, 7) > 0 and x > 0:
#         print(s)
#         break