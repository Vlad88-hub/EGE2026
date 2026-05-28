with open(r'./files/23368.txt') as file:
    data = [list(map(int, i.split())) for i in file]

for pos, line in enumerate(data, start=1):
    amount = [line.count(n) for n in set(line)]
    pov = [n for n in line if line.count(n) != 1]
    ne_pov = [n for n in line if line.count(n) == 1]
    if sorted(amount) == [1,1,1,2,2] and (sum(pov) / len(pov)) < max(ne_pov):
        print(pos)
        break