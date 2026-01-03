with open(r'.\files\24_1428.txt') as file:
    data = file.readline()

data = data.replace('XY', 'X Y')
data = data.replace('XZ', 'X Z')
data = data.split()

print(len(max(data, key=len)))