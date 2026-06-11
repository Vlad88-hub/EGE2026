with open(r'../files/26_17565.txt') as file:
    N, S = map(int, file.readline().split())
    kand = []
    for i in file:
        idd, x, y, z, s = map(int, i.split())
        kand.append([idd, x + y + z, s])

kand = sorted(kand, key=lambda x: (-x[1],-x[2], x[0]))

pol = kand[:S][-1][1]
cnt_pol = len([i for i in kand if i[1] == pol])

cnt_pol_kand = sum(k[1] == pol for k in kand[:S])

# print(kand[:S])
# print(kand)

print(cnt_pol, 7600410)

###############################################

with open(r'../files/26_17565.txt') as file:
    N, S = map(int, file.readline().split())
    kand = []
    for i in file:
        idd, x, y, z, s = map(int, i.split())
        kand.append([ x + y + z,s,idd])

kand = sorted(kand, key=lambda x: (-x[0],-x[1], x[2]))

full_score_id = 0
cnt_half_score = 0
half_score = kand[:S][-1][0]
if half_score == kand[S:][0][0]:
    cnt_half_score = sum(st[0] == half_score for st in kand)
    full_score_id = [st[2] for st in kand if st[0] > half_score][-1]
else:
    full_score_id = kand[:S][-1][2]

print(full_score_id, cnt_half_score)

