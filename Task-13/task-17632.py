from ipaddress import *

def f(ip):
    ip = f'{int(ip):032b}'
    return ip.count('1') % 5 == 0

net = ip_network('112.160.0.0/255.240.0.0', False)

cnt = 0
for ipp in net:
    F = f(ipp)
    if F:
        cnt += 1

print(cnt)