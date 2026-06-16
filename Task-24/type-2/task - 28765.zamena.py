with open(r'../files/24_28765.txt') as file:
    data = file.readline()

data = data.replace('BC', 'B C')
data = data.split()

max_ans = 0
for i in range(1, len(data) - 180):
    line = ''.join(data[i:i + 181])
    max_ans = max(max_ans, len(line))

print(max_ans)