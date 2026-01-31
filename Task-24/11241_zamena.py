from idlelib.replace import replace

with open(r'.\files\24_11241.txt') as file:
    data = file.readline()

for i in 'ABCD':
    data = data.replace(i, ' ')

data = data.split()

print(len(max(data, key=len)))