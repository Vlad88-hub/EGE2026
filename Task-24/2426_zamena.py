with open(r'.\files\24_2426.txt') as file:
    data = file.readline()

for i in 'ABC':
    data = data.replace(i, ' ')
data = data.split()
print(len(max(data, key=len)))