for n in range(10_000, 3, -1):
    s = '7' + '3'*n

    while '73' in s or '3333' in s or '1133' in s:
        if '73' in s:
            s = s.replace('73', '11', 1)
        if '3333' in s:
            s = s.replace('3333', '7', 1)
        if '1133' in s:
            s = s.replace('1133', '37', 1)

    if sum(int(x) for x in s) == 128:
        print(n) 
        break

# for n in range(4, 10_000):
#   s = '7' + '3'*n
#   while '73' in s or '3333' in s or '1133' in s:
#     if '73' in s:
#       s = s.replace('73', '11', 1)
#     if '3333' in s:
#       s = s.replace('3333', '7', 1)
#     if '1133' in s:
#       s = s.replace('1133', '37', 1)
#   sm = sum(int(x) for x in s)
#   if sm == 128:
#     print(n)