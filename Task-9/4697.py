with open(r'.\files\4697.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for line in data:
    amount = [line.count(i) for i in set(line)]
    pov = [n for n in set(line) if line.count(n) != 1]
    ne_pov = [n for n in set(line) if line.count(n) == 1]
    if sorted(amount) == [1,1,1,1,2] and sum(ne_pov) / len(ne_pov) <= pov[0]*2:
        cnt += 1

print(cnt)