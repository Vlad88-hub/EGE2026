from ipaddress import *

def f(ip):
    ip = f'{int(ip):032b}'
    return ip[16:23].count('0') > ip[24:].count('0')

cnt = 0
for A in range(0, 255):
    net = ip_network(f'246.81.65.{A}/255.255.255.224', False)
    # for ip in net:
    #     ip = f'{int(ip):032b}'
    #     print(ip)
    #     break
    if all(f(ip) for ip in net):
        for ip in net:
            print(f'{int(ip):032b}')
        cnt += 1

print(cnt)
# data = ip_address('255.234.12.0')
# print(data[:2])