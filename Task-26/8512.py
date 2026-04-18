with open(r'./files/26_8512.txt') as file:
    K = int(file.readline())
    N = int(file.readline())
    passengers = [list(map(int, i.split())) for i in file]

passengers = sorted(passengers)
cell = [0] * K
last_cells = 0
cnt = 0

for time in passengers:
    for i in range(K):
        if cell[i] < time[0]:
            cell[i] = time[1]
            cnt += 1
            last_cells = i + 1
            break

print(cnt, last_cells)