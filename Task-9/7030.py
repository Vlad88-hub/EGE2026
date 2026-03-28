with open(r'.\files\7030.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for line in data:
    amount = [line.count(i) for i in set(line)]
    u = [n for n in set(line) if line.count(n) != 1]
    if sorted(amount) == [2,2,2] and max(u)**2 == min(u)**2 + (sum(u) - min(u) - max(u))**2:
        cnt += 1

print(cnt)