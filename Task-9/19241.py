with open(r'.\files\19241.txt') as file:
    data = [list(map(int, i.split())) for i in file]

ans = []
for pos, line in enumerate(data, start=1):
    amount = [line.count(i) for i in set(line)]
    pov = [n for n in set(line) if line.count(n) != 1]
    ne_pov = [n for n in set(line) if line.count(n) == 1]
    if sorted(amount) == [1, 3, 3] and sum(pov) / len(pov) < ne_pov[0]:
        ans.append(pos)

print(ans[-1])