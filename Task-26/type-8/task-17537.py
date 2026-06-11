with open(r'../files/26_17537.txt') as file:
    N, M, K = map(int,file.readline().split())
    places = [list(map(int, i.split())) for i in file]

seats = [M] * (K+1)
for mes in places:
    seats[mes[1]] = min(mes[0] - 1, seats[mes[1]])

last_row = []
for i in range(1, K):
    last_row += [[min(seats[i], seats[i+1]), i+1]]

print(max(last_row))




