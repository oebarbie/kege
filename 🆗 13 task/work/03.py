from ipaddress import *

ip = ip_address('115.53.128.88')
for mask in range(31):
    net1 = ip_network('115.53.128.0/' + str(mask), 0)
    if str(net1[0]) == '115.53.128.0' and net1[0] < ip < net1[-1]:
        if net1.num_addresses -2 >= 1000:
            print(net1.netmask)
