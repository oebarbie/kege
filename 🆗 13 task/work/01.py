from ipaddress import *

# ip_address ('IP')
# net = ip_network('IP/mask, 0|1)
#   net.hosts() - список всех узлов сети
#   net.num_addresses - количество адресов в сети
# int(IP) - число
# номер компьютера - номер узла = ip - адрес сети

net = ip_network('192.168.156.235/255.255.255.240', 0)
ip = ip_address('192.168.156.235')
mask = ip_address('255.255.255.240')
net_address = int(ip) & int(mask)
print(int(ip) - net_address)

# net.hostmask - маска для определения номера узла
# net.netmask - маска для определения адреса сети

ip = ip_address('192.168.156.235')
net = ip_network('192.168.156.235/255.255.255.240', 0)
#print(int(ip) & int(net.hostmask))
# номер узла = IP - адрес сети
print(int(ip) - int(net.network_address))


k = 0
for ip1 in net:
  if ip1 == ip:
    print(' ', k)
  k+= 1