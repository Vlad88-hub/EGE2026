with open(r'../files/24_1975.txt') as file:
    data = file.readline()

while 'PP' in data:
    data = data.replace('PP', 'P P')

data = data.split()

ans = 0
for i in data:
    ans = max(ans, len(i))

print(ans)