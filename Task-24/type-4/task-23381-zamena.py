with open(r'../files/24_23381.txt') as file:
    data = file.readline()

for i in '02468':
    data = data.replace(i, '* *')

data = data.split()

ans = 0
for line in data[1:-1]:
    if all(i not in line for i in '13579'):
        u = len(set(line)) == 2
        if u:
            ans = max(ans, len(line))

print(ans)
