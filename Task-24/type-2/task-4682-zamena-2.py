with open(r'../files/24_4682.txt') as file:
    data = file.readline()

for i in 'AE':
    for j in 'BCD':
        data = data.replace(i+j, '*')

for i in 'ABCDE':
    data = data.replace(i, ' ')

data = data.split()

print(len(max(data, key=len)))