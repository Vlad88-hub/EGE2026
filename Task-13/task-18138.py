from ipaddress import *

for mask in range(1, 31):
    net = ip_network(f'172.16.168.0/{mask}', False)
    if sum(str(ipp).count('0') % 7 == 0 for ipp in list(net.hosts())) == 35:
        print(mask)

