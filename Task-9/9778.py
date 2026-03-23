with open(r'.\files\9778.txt') as file:
    data = [list(map(int, i.split())) for i in file]

for pos, line in enumerate(data, start=1):
    amount = [line.count(i) for i in set(line)]
    sum1 = [n for n in set(line) if line.count(n) == 1]
    sum2 = [n for n in set(line) if line.count(n) != 1]
    if sorted(amount) == [1,1,1,1,2] and sum2[0] >= sum(sum1) / len(sum1):
        print(pos)
        break

