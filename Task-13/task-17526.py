from ipaddress import *

def f(ip):
    ip = f'{int(ip):032b}'
    return ip.count('1') % 2 != 0

net = ip_network('172.16.128.0/255.255.192.0', False)

cnt = 0
for ipp in net:
    F = f(ipp)
    if F:
        cnt += 1
print(cnt)
