with open(r'../files/24-293.txt') as file:
    data = file.readline()

data = data.split('D')

ans = 0
for i in range(len(data) - 100):
    line = 'D'.join(data[i:i+101])
    if all(i not in line for i in '0123456789') and 'DS' not in line and 'DS' not in line:
        ans = max(ans, len(line))

print(ans)