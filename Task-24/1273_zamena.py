with open(r'.\files\24_1273.txt') as file:
    data = file.readline()

data = data.replace('XYZ', 'XY YZ')
data = data.split()
print(len(max(data, key=len)))