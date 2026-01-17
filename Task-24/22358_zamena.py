from string import digits, ascii_uppercase

with open(r'.\files\24_22358.txt') as file:
    data = file.readline()

alph = digits + ascii_uppercase

data_2 = data
for i in alph[12:]:
    data_2 = data_2.replace(i, ' ')
while '0' in data_2:
    data_2 = data_2.replace('0', ' ')

data_2 = data_2.split()

ans = '0'
for match in data_2:
    if match and int(match, 12) % 3 == 0:
        if len(ans) < len(match):
            ans = match
        elif len(ans) == len(match) and int(ans, 12) < int(match, 12):
            ans = match
    elif match:
        for i in range(len(match)):
            for j in range(len(match), i, -1):
                line = match[i:j].lstrip('0')
                if line and int(match, 12) % 3 == 0:
                    if len(ans) < len(line):
                        ans = line
                        break
                    elif len(ans) == len(line) and int(ans, 12) < int(line, 12):
                        ans = line

print(data.find(ans))