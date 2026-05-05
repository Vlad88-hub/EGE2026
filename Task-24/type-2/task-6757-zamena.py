with open(r'../files/24_6757.txt') as file:
    data = file.readline()

for i in ['CFE', 'FCE']:
    data = data.replace(i, '*')

for i in 'CDEF':
    data = data.replace(i, ' ')

data = data.split()

print(len(max(data, key=len)))