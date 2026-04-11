from ipaddress import *

ip_1 = ip_address('216.54.187.235')
ip_2 = ip_address('216.54.174.128')

for mask in range(16, 31):
    net = ip_network(f'{ip_2}/{mask}', False)
    if ip_1 not in net.hosts() and ip_2 in net.hosts():
        print(mask)
