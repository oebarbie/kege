from ipaddress import *

# ip = ip_address('192.168.32.160')
# mask = ip_address('255.255.255.240')
# net = int(ip) & int(mask)
net = ip_network('192.168.32.160/255.255.255.240', 0)
print(net)
cnt = 0
for ip in net:
    # двоичное представление ip адреса
    if bin(int(ip))[2:].zfill(32).count('1') % 2 == 0:
        cnt += 1
print(cnt)