from ipaddress import *

def f(ip):
    ip = f'{int(ip):032b}'
    return ip[16:24].count('0') > ip[24:].count('0')

cnt = 0
for A in range(0, 255):
    ip_host = ip_address(f'246.81.65.{A}')
    net = ip_network(f'{ip_host}/255.255.255.224', False)
    # for ip in net:
    #     ip = f'{int(ip):032b}'
    #     print(ip)
    #     break
    if ip_host in net.hosts() and all(f(ip) for ip in net.hosts()):
        for ip in net:
            print(f'{int(ip):032b}')
        cnt += 1

print(cnt)
# data = ip_address('255.234.12.0')
# print(data[:2])