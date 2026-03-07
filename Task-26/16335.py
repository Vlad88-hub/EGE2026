with open(r'.\files\26_16335.txt') as file:
    N = int(file.readline())
    cakes = [int(i) for i in file]

cakes = sorted(cakes, reverse = True)

all_cake = [cakes[0]]

for cake in cakes:
    if all_cake[-1] - cake >= 4:
        all_cake.append(cake)

print(len(all_cake), all_cake[-1])