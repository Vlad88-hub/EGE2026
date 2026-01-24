from string import digits, ascii_uppercase

with open(r'.\files\24_10724.txt') as file:
    data = file.readline()

# data = 'PZ5GRLU8SXS95V7IDX5K22RFEI1A56YBNTGQPRSH54CYQA3OJ26NQ2Z44O4AVYFFWEW00000000000BX'

alph = digits + ascii_uppercase

for i in alph[16:]:
    data = data.replace(i, ' ')

data = data.split()

ans = []
for num in data:
    num = num.lstrip('0')
    ans.append(num)

print(len(max(ans, key=len)))
