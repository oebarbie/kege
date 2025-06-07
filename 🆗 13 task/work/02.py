from ipaddress import *

ip1 = ip_address('112.117.107.70')
ip2 = ip_address('112.117.121.80')
for mask in range(31):
##  net1 = ip_network(f'{ip1}/{mask}', 0)
##  net2 = ip_network(f'{ip2}/{mask}', 0)
  net1 = ip_network('112.117.107.70/'+str(mask), 0)
  net2 = ip_network('112.117.121.80/'+str(mask), 0)
  if net1 == net2 and net1[0] < ip1 < net1[-1] and net2[0] < ip2 < net2[-1]:
    print(net1.netmask)