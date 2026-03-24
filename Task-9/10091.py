with open(r'.\files\10091.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for line in data:
    amount = [line.count(i) for i in set(line)]
    pov = [n for n in set(line) if line.count(n) != 1]
    if sorted(amount) == [1,1,1,2,2] and sum(pov) / len(pov) < sum(line) / len(line):
        cnt += 1

print(cnt)