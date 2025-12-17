with open(r'.\files\24_1975.txt') as files:
    data = files.readline()

while 'PP' in data:
    data = data.replace('PP', 'P P')


data = data.split()
print(len(max(data, key=len)))