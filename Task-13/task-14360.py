from ipaddress import *

ip_1 = ip_address('153.202.16.37')

for mask in range(16, 31):
    net = ip_network(f'{ip_1}/{mask}', False)
    if ip_1 in net.hosts() and net.network_address == ip_address('153.202.16.32'):
        print(sum(map(int, str(net.netmask).split('.')[-2:])))