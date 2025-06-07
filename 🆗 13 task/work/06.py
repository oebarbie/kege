from ipaddress import *

for mask in range(31):
    net = ip_network('220.128.112.142/'+str(mask), 0)
    if str(net.network_address) == '220.128.96.0':
        # (net[0])
        print(net.netmask)