with open(r'../files/24-371.txt') as file:
    data = file.readline()

dat = '***M ***M.**M***M ** M **.***MM****..***** '
data = data.replace(' ', '!')
data = data.replace('M', ' ')
data = data.split()

ans = 0
for i in range(len(data) - 112):
    line = 'M'.join(data[i:i+113])
    if line.count('.') > 0:
        while line[-1] != '.':
            line = line[:-1]
    if line.count('M') == 112 and line.count('.') == 1:
        print(line)
        ans = max(ans, len(line))
# print(dat[:-1])

print(ans)