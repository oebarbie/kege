s = 'x'*107

while 'xxx' in s or 'zyx' in s or 'zxx' in s:
    s = s.replace('xxx', 'zz', 1)
    s = s.replace('zyx', 'x', 1)
    s = s.replace('zxx', 'y', 1)

print(s)