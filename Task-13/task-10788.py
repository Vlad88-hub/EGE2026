from ipaddress import *

def f(ip):
    ip = f'{int(ip):032b}'
    return ip.count('1') >= 5

ip_1 = ip_address('201.44.240.33')
ip_2 = ip_address('201.44.240.107')

cnt = 0
for mask in range(16, 31):
    net = ip_network(f'{ip_1}/{mask}', False)
    if ip_1 in net.hosts() and ip_2 in net.hosts():
        F = f(net.network_address)
        if F:
            print(mask)

print(cnt)
