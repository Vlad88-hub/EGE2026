with open(r'.\files\26.2_19727.txt') as file:
    V, N = map(int, file.readline().split())
    cans = [int(i) for i in file]

cans = sorted(cans)
max_list_can = []

for can in cans:
    if sum(max_list_can) + can < V:
        max_list_can.append(can)

max_list_can =max_list_can[:-1]
free_space = V - sum(max_list_can)

cnt = 0
for n in cans:
    if n > free_space:
        cnt += 1

print(len(max_list_can) + 1 ,sum(i > free_space for i in cans), cnt)