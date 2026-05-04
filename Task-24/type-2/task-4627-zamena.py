with open(r'../files/24_4627.txt') as file:
    data = file.readline()

for i in ['NPO', 'PNO']:
    data = data.replace(i, '*')

for i in 'NPO':
    data = data.replace(i, ' ')

data = data.split()

print(len(max(data, key=len)))