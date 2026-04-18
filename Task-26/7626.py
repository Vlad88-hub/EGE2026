with open(r'./files/26_7626.txt') as file:
    K = int(file.readline())
    N = int(file.readline())
    passengers = [list(map(int, i.split())) for i in file]

passengers = sorted(passengers)
cells = [0] * K
last_cells = 0
cnt = 0

for time in passengers:
    for i in range(K):
        if cells[i] < time[0]:
            cells[i] = time[1]
            cnt += 1
            last_cells = i + 1
            break

print(cnt, last_cells)