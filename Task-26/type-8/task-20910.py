with open(r'../files/26_20910.txt') as file:
    N, M, K = map(int, file.readline().split())
    places = [list(map(int, i.split())) for i in file]

mes = [10**10] * (K+1)
for pl in places:
    mes[pl[1]] = min(mes[pl[1]], pl[0]-1)

max_row = []
for i in range(1, K):
    max_row.append([min(mes[i], mes[i+1]), i])

print(max(max_row))