with open(r'../files/24-371.txt') as file:
    data = file.readline()

dat = '***M ***M.**M***M ** M **.***MM****..***** '
data = data.split('M')

ans = 0
for i in range(len(data) - 112):
    line_1 = data[i] + 'M'
    line_112 = 'M'.join(data[i+1:i+112]) + 'M'
    line_113 = data[i+112]
    if '.' not in line_112:
        if '.' in line_1:
            line_1 = line_1[line_1.rfind('.'):]
        if '.' in line_113:
            line_113 = line_113.find('.')
        ans = max(ans, len(line_1)+len(line_112)+line_113+1)

#     if line.count('.') > 0:
#         while line[-1] != '.' and line.count('.') != 1:
#             line = line[:-1]
#     if line.count('M') == 112 and line.count('.') == 1:
#         # print(line)
#         ans = max(ans, len(line))
# # print(dat[:-1])

print(ans)

################################################################

with open(r'../files/24-371.txt') as file:
    data = file.readline()

data = data.replace('.', ',*')
data = data.split('*')[:-1]

ans = 0
for line in data:
    cnt_M = line.count('M')
    if cnt_M == 112:
        ans = max(ans, len(line))
    elif cnt_M>112:
        while cnt_M>112:
            if line[0] == 'M' : cnt_M -= 1
            line = line[1:]
        ans = max(ans, len(line))

print(ans)