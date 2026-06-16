with open(r'../files/24_19254 (1).txt') as file:
    data = file.readline()

data = data.replace('FSRQ', '*** ***')
data = data.split()

max_ans = 0
for i in range(len(data) - 80):
    line = ''.join(data[i: i + 81]).replace('******', 'FSRQ')
    max_ans = max(max_ans, len(line))

print(max_ans)