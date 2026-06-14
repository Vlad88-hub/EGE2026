from ipaddress import *

ip_1 = ip_address('153.202.16.37')

for mask in range(24, 33):
    net = ip_network(f'{ip_1}/{mask}', False)
    print(net.network_address)
    print(net.netmask)