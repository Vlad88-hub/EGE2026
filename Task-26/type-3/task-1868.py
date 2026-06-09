with open(r'../files/26_1868.txt') as file:
    N = file.readline()
    # r = dict()
    # for i in file:
    #     row, seat = map(int, i.split())
    #     if row not in r:
    #         r[row] = [seat]
    #     else:
    #         r[row] += [seat]

    rab = [list(map(int, i.split())) for i in file]

rab = sorted(rab, key=lambda x: (-x[0], x[1]))

# ans = []
for i1, i2 in zip(rab, rab[1:]):
    if i1[0] == i2[0]:
        if i2[1] - i1[1] == 3:
            print(i1[0], i1[1]+1)
            break

# max_ans = max(ans)[0]
# new_ans = []
# for a in ans:
#     if a[0] == max_ans:
#         new_ans.append(a[1])
#
# print(max_ans, min(new_ans))