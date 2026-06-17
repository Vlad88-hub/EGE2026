with open(r'../files/24_27634.txt') as file:
    data = file.readline()

data = data.split('Z')

min_ans = 10**10
for i in range(len(data) - 268):
    line = 'Z' + 'Z'.join(data[i:i+269]) + 'Z'
    min_ans = min(min_ans, len(line))

print(min_ans)