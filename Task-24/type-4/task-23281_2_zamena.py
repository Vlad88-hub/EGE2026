with open(r'../files/24_23381.txt') as file:
    data = file.readline()

for i in '02468':
    data = data.replace(i, ' ')

data = data.split()

max_len = 0
for line in data[1:-1]:
    if all(i not in '13579' for n in line) and len(set(line)) == 1:
        max_len = max(max_len, len(line) +2)

print(max_len)