with open(r'./files/24346.txt') as file:
    data = [list(map(int, i.split())) for i in file]

for pos, line in enumerate(data, start=1):
    # amount = [line.count(n) for n in set(line)]
    pov = [n for n in line if line.count(n) != 1]
    ne_pov = [n for n in set(line) if line.count(n) == 1]
    if pov and ne_pov and sum(pov)**2 > sum(ne_pov)**2 and sum(line) % 2 != 0:
        print(pos)
