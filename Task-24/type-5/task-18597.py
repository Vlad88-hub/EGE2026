from asyncio import new_event_loop

with open(r'../files/24_18597.txt') as file:
    data = file.readline()

data = data.split('&')
ans = 0
for line1, line2 in zip(data, data[1:]):
    if '.' not in line1 or '.' not in line2:
        continue

    pos_dot2_1 = line2.find('.')
    if len(line2[:pos_dot2_1]) != 4 or line2[0] =='0':
        continue
    pos_dot2_2 = line2.find('.', pos_dot2_1 + 1)
    if pos_dot2_2 == -1 and line2[-1] == '.':
        continue
    if pos_dot2_2 != -1:
        line2 = line2[:pos_dot2_2]
        if line2[-1] == '.':
            continue

    pos_dot1 = line2.rfind('.')
    if pos_dot1 < 4 or pos_dot1 == len(line1) - 1:
        continue
    line1 = line1[pos_dot1 - 4:]
    if '.' in line1[:4] or line1[0] == '0':
        continue

    ans = max(ans, len(line1) + len(line2) + 1)

print(ans)
