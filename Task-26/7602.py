with open(r'./files/26_7602.txt') as file:
    K = int(file.readline())
    N = int(file.readline())
    passengers = [list(map(int, i.split())) for i in file]

# data = sorted(passengers)
# store = [data[0]]
#
# cnt_2 = 0
# last = 0
# for d in range(len(data) + 1):
#     if len(store) < K:
#         for s in range(len(store)):
#             if data[d][0] - store[s][1] >= 1:
#                 store[s] = data[d]
#                 cnt_2 += 1
#                 last = len(store[:s])
#                 break
#         else:
#             store += [data[d]]
#             cnt_2 += 1
#             last = len(store)
#
# print(cnt_2, last)


passengers = sorted(passengers)
cells = [0] * K
last_cell = 0
cnt = 0

for time in passengers:
    for i in range(K):
        if cells[i] < time[0]:
            cells[i] = time[1]
            cnt += 1
            last_cell = i + 1
            break


print(cnt, last_cell)
