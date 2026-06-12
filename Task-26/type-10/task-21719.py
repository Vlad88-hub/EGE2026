with open(r'../files/26_21719.txt') as file:
    N = int(file.readline())
    stud = {}
    for i in file:
        idd, num = map(int, i.split())
        if idd not in stud:
            stud[idd] = [num]
        elif num in stud[idd]:
            continue
        else:
            stud[idd] += [num]

comp = []
for idd in stud:
    cnt_num = 1
    stud[idd] = sorted(stud[idd])
    for i in range(len(stud[idd]) - 1):
        if stud[idd][i+1] - stud[idd][i] == 2:
            cnt_num += 1
        else:
            comp.append([cnt_num, idd])
            cnt_num = 1
    comp.append([cnt_num, idd])

    # comp.append([idd, cnt_num])

print(min(comp, key=lambda x: (-x[0], x[1])))




# print(max_num, min_stud_id)


# comp = {}
# for idd in stud:
#     cnt_num = 1
#     stud[idd] = sorted(stud[idd])
#     for i in range(len(stud[idd]) - 1):
#         if stud[idd][i+1] - stud[idd][i] == 2:
#             cnt_num += 1
#         else:
#             cnt_num = 1
#         if idd not in comp:
#             comp[idd] = cnt_num
#         else:
#             comp[idd] = max(cnt_num, comp[idd])

# max_num = max(comp[idd] for idd in comp)
# comp = sorted(comp)

# min_stud_id = min(idd for idd in comp if comp[idd] == max_num)