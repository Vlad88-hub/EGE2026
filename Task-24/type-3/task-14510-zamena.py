from re import sub

with open(r'../files/24_14510.txt') as file:
    data = file.readline()

data = sub(r'[^AEIOUY]{2}[AEIOUY]', '*', data)
data = data.split('*')

ans = 10**10
for i in range(1, len(data) - 498 - 1):
    line = len('***'.join(data[i:i+499])) + 6
    ans = min(ans, line)

print(ans)












# for i in 'AEIOUY':
#     data = data.replace(i, '*')
#
# for i in data:
#     if i