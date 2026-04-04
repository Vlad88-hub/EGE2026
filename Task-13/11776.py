# ip = bin(66)[2:]
# print(ip)
# print(int(ip) % 20)

from ipaddress import *

net = ip_network('235.86.56.0/255.255.248.0', False)

cnt = 0
for ip in net:
    ip = f'{int(ip):032b}'
    if int(ip) % 20 == 11:
        cnt += 1

print(cnt)