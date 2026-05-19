with open(r'../files/24_18186.txt') as file:
    data = file.readline()

dt = '***" "***AAAAAAAAA***" "***AA***" "***AABAA***" "***A'
dat = 'BBAAAAAAABBAAABBAAABAABBAA'

for i_1 in 'BCDFGH':
    for i_2 in 'BCDFGH':
        for i_3 in 'AE':
            data = data.replace(i_1+i_2+i_3, '*** ***')

data = data.split()

ans = 0
for line in data[1:]:
    if line[-3:] == '***':
        ans = max(ans, len(line))

print(ans)
# print(data[-3:])