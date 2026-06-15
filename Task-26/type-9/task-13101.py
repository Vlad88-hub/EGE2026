# with open(r'../files/26_13101.txt') as file:
#     N = int(file.readline())
#     clients = [list(map(int, i.split())) for i in file]
#
# clients = sorted(clients)
#
# chek_1 = []
# chek_2 = []
# cnt_comp_client = 0
# cnt_chek_2 = 0
# for client in clients:
#
#     if client[2] == 1:
#         if len(chek_1) < 13:
#             cnt_comp_client += 1
#             chek_1.append(client[0] + client[1])
#         elif len(chek_1) == 13:
#             cnt_comp_client += 1
#             cnt_blow = 0
#             for ch in chek_1:
#                 if ch <= client[0]:
#                     cnt_blow += 1
#             chek_1 = chek_1[cnt_blow:]
#             chek_1.append(client[0] + client[1])
#         else:
#             cnt_blow_2 = 0
#             for ch in chek_1:
#                 if ch <= client[0]:
#                     cnt_blow_2 += 1
#             if cnt_blow_2 == 0:
#                 continue
#             else:
#                 cnt_comp_client += 1
#                 chek_1 = chek_1[cnt_blow_2:]
#                 chek_1.append(client[0] + client[1])
#
#
#     if client[2] == 2:
#         if len(chek_2) < 13:
#             cnt_chek_2 += 1
#             cnt_comp_client += 1
#             chek_2.append(client[0] + client[1])
#         elif len(chek_2) == 13:
#             cnt_chek_2 += 1
#             cnt_comp_client += 1
#             cnt_blow = 0
#             for ch in chek_2:
#                 if ch <= client[0]:
#                     cnt_blow += 1
#             chek_2 = chek_2[cnt_blow:]
#             chek_2.append(client[0] + client[1])
#         else:
#             cnt_blow_2 = 0
#             for ch in chek_2:
#                 if ch <= client[0]:
#                     cnt_blow_2 += 1
#             if cnt_blow_2 == 0:
#                 continue
#             else:
#                 cnt_comp_client += 1
#                 cnt_chek_2 += 1
#                 chek_2 = chek_2[cnt_blow_2:]
#                 chek_2.append(client[0] + client[1])
#
#
#     if client[2] == 0:
#         if len(chek_1) < len(chek_2):
#             if len(chek_1) < 13:
#                 cnt_comp_client += 1
#                 chek_1.append(client[0] + client[1])
#             elif len(chek_1) == 13:
#                 cnt_comp_client += 1
#                 cnt_blow = 0
#                 for ch in chek_1:
#                     if ch <= client[0]:
#                         cnt_blow += 1
#                 chek_1 = chek_1[cnt_blow:]
#                 chek_1.append(client[0] + client[1])
#             else:
#                 cnt_blow_2 = 0
#                 for ch in chek_1:
#                     if ch <= client[0]:
#                         cnt_blow_2 += 1
#                 if cnt_blow_2 == 0:
#                     continue
#                 else:
#                     cnt_comp_client += 1
#                     chek_1 = chek_1[cnt_blow_2:]
#                     chek_1.append(client[0] + client[1])
#         else:
#             if len(chek_2) < 13:
#                 cnt_chek_2 += 1
#                 cnt_comp_client += 1
#                 chek_2.append(client[0] + client[1])
#             elif len(chek_2) == 13:
#                 cnt_chek_2 += 1
#                 cnt_comp_client += 1
#                 cnt_blow = 0
#                 for ch in chek_2:
#                     if ch <= client[0]:
#                         cnt_blow += 1
#                 chek_2 = chek_2[cnt_blow:]
#                 chek_2.append(client[0] + client[1])
#             else:
#                 cnt_blow_2 = 0
#                 for ch in chek_2:
#                     if ch <= client[0]:
#                         cnt_blow_2 += 1
#                 if cnt_blow_2 == 0:
#                     continue
#                 else:
#                     cnt_comp_client += 1
#                     cnt_chek_2 += 1
#                     chek_2 = chek_2[cnt_blow_2:]
#                     chek_2.append(client[0] + client[1])
#
#
# print(cnt_chek_2, N - cnt_comp_client)

#############################################################

with open(r'../files/26_13101.txt') as file:
    N = int(file.readline())
    clients = [list(map(int, i.split())) for i in file]

clients = sorted(clients)

queue = {1:[], 2:[]}
cnt = skip = 0
for enter, time, ID in clients:
    for i in 1, 2:
        for client in queue[i].copy():
            if client <= enter:
                queue[i].remove(client)
                if i == 2:
                    cnt += 1
    if not ID:
        ID = min(queue, key=lambda x: (len(queue[x]), x))

    if len(queue[ID]) == 14:
        skip += 1
        continue
    if queue[ID]:
        queue[ID].append(queue[ID][-1] + time)
    else:
        queue[ID].append(enter + time)

for i in 1, 2:
    for client in queue[i].copy():
        queue[i].remove(client)
        if i == 2:
            cnt += 1

print(cnt, skip)