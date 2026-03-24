with open(r'.\files\21704.txt') as file:
    data = [list(map(int, i.split())) for i in file]

for line in data:
    not_max_or_min = [i for i in line if i != max(line) and i != min(line)]
    if sorted(line, reverse=True) == line and max(line) + min(line) / 2 > sum(not_max_or_min) / len(not_max_or_min):
        print(sum(line))
        break