from ipaddress import *

net = ip_network('191.128.66.83/255.192.0.0', False)

for ip in net:
    print(ip)

print('191.191.255.255')