from ipaddress import *

net = ip_network('102.162.200.51/255.255.255.0', False)

print(list(net.hosts())[-1])
print(102+162+200+254)