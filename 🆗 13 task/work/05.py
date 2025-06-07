from ipaddress import *

cnt = 0
net = ip_network('123.222.111.192/255.255.255.248', 0)
for ip in net:
    s = bin(int(ip))[2:].zfill(32)
    # взять последние 8 бит
    b4 = s[-8:]
    if b4.count('1') % 3 != 0:
        cnt += 1
print(cnt)
