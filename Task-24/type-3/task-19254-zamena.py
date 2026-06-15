with open(r'../files/24_19254 (1).txt') as file:
    data = file.readline()

data = data.split('FSRQ')

max_ans = 0
for i in range(len(data) - 80):
    line = 'FSRQ'.join(data[i: i + 81])
    max_ans = max(max_ans, len(line) + 6)

print(max_ans)