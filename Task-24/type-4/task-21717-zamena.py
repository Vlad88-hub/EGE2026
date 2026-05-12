with open(r'../files/24_21717.txt') as file:
    data = file.readline()

data = data.split('RSQ')

ans = 10000000
for i in range(len(data) - 130):
    line = 'RSQ'.join(data[i:i+130])
    pos_Q = data[i+129].find('Q')
    ans = min(ans, len(line) + 3 + pos_Q)

print(ans)