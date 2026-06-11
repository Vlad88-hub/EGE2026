with open(r'../files/26_9847.txt') as file:
    N = file.readline()
    pos = [list(map(int, i.split())) for i in file]

new_pos = []
for p1, p2 in pos:
    for i in range(p1, p2):
        new_pos.append(i)

new_pos = sorted(new_pos)

ans = []
cnt = 1
for i1, i2 in zip(new_pos, new_pos[1:]):
    if i2 == i1:
        cnt += 1
    else:
        ans.append(cnt)
        cnt = 1
max_ans = max(ans)

sum_max_ans = 0
x=0
for i in range(len(ans)):
    if i < x:
        continue
    if ans[i] == max_ans:
        sum_max_ans += 1
        for j in range(i, len(ans)):
            if ans[i] == ans[j]:
                x = j

print(sum_max_ans, max_ans)

##################################################

with open(r'../files/26_9847.txt') as file:
    N = file.readline()
    pos = [list(map(int, i.split())) for i in file]

pos = sorted(pos)
shop = [0] * 1440

for p_l, p_r in pos:
    for i in range(p_l, p_r):
        shop[i] += 1

max_shop = max(shop)

sum_max_shop = 0
x=0
for i in range(len(shop)):
    if i < x:
        continue
    if shop[i] == max_shop:
        sum_max_shop += 1
        for j in range(i, len(ans)):
            if shop[i] == shop[j]:
                x = j

print(sum_max_shop, max_shop)

