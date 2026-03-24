with open(r'.\files\23747.txt') as file:
    data = [list(map(int, i.split())) for i in file]

for line in data[::-1]:
    amount = [line.count(n) for n in set(line)]
    pov = [n for n in set(line) if line.count(n) != 1]
    ne_pov = [n for n in set(line) if line.count(n) == 1]
    if sorted(amount) == [1,1,1,1,3] and sum(ne_pov) / len(ne_pov) <= pov[0]:
        print(sum(line))
        break