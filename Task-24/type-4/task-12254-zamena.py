with open(r'../files/24_12254.txt') as file:
    data = file.readline()

data = data.replace('RSQ', '***')
data = data.replace('SQ*', ' ***')
data = data.replace('Q*', ' **')
data = data.replace('*RS', '*** ')
data = data.replace('*R', '** ')

for i in 'RSQ':
    data = data.replace(i, ' ')

data = data.split()

print(len(max(data, key=len)))