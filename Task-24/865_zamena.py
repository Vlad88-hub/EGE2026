with open(r'.\files\24_865.txt') as file:
    data = file.readline()

test = 'ABAAACABFCCCDADFF'


for i in 'CF':
    data = data.replace(i, ' ')

data = data.split()
print(len(max(data, key=len)))