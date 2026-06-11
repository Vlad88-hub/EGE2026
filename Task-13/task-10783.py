from ipaddress import *

ip_1 = ip_address('121.171.5.70')
ip_2 = ip_address('121.171.5.107')

for mask in range(24, 32):
    net = ip_network(f'{ip_1}/{mask}', False)
    if ip_2 in net.hosts() and ip_1 in net.hosts():
        print(len(list(net.hosts())))