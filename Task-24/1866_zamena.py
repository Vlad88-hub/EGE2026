from os.path import split

with open(r'.\files\24_1866.txt') as file:
    data = file.readline()

data = data.replace('ad', 'a d')
data = data.replace('da', 'd a')
data = data.split()

print(len(max(data, key=len)))