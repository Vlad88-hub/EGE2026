with open(r'./files/26_17643.txt') as file:
    N = file.readline()
    data = [list(map(int, i.split())) for i in file]


sum_avs = []
for i in data:
    sum_avs += [i[1]]
sum_avs = sum(sum_avs)/len(sum_avs)

new_data = [i for i in data if i[1] > sum_avs]

idd = set(i[0] for i in new_data)

maxx_id = []
for i in idd:
    cnt_0 = 0
    for n in new_data:
        if n[0] == i and n[2] == 0:
            cnt_0 += 1
    maxx_id.append([cnt_0, i])

max_id = max(maxx_id)[0]
m = [idd[1] for idd in maxx_id if idd[0] == max_id]
new_m = [46481, 51786]
leader_1 = [n for n in new_data if n[0] == new_m[0]]
leader_2 = [n for n in new_data if n[0] == new_m[1]]

cnt_leader_1 = [n for n in leader_1 if n[2] == 1]
cnt_leader_2 = [n for n in leader_2 if n[2] == 1]

true_leader_id = 46481
# print(len(cnt_leader_1) - len(cnt_leader_2))

sum_lead = 0
cnt_lead = 0
for i in new_data:
    if i[0] == true_leader_id:
        if i[2] == 0:
            sum_lead += i[1]
        else:
            cnt_lead += 1

print(sum_lead, cnt_lead)


###########################################################

with open(r'./files/26_17643.txt') as file:
    N = int(file.readline())
    goods = [list(map(int, i.split())) for i in file]

avg = sum(i[1] for i in goods) / N
# exp = [i for i in data if i[1] > avg]
exp = {}
for good in [i for i in goods if i[1] > avg]:
    if good[0] not in exp:
        exp[good[0]] = [not good[2], good[1], good[2]]
    else:
        exp[good[0]][0] += not good[2]
        exp[good[0]][2] += good[2]

exp = sorted(exp.values(), key= lambda x: (-x[0], -x[1], x[2]))[0]

print(exp[0] * exp[1], exp[2])