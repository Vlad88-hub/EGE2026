from string import printable

with open(r'../files/24_21908.txt') as file:
    data = file.readline().lower()

for i in printable[14:]:
    data = data.replace(i, ' ')

data = data.split()

ans = []
for line in data:
    line = line.rstrip('13579bd').lstrip('0')
    if line:
        ans.append(line)


print(len(max(ans, key=lambda x: int(x, 14))))