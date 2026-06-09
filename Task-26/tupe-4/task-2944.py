with open(r'../files/26_2944.txt') as file:
    S, N = map(int, file.readline().split())
    per = [int(i) for i in file]

per = sorted(per)

pers = [0]
for p in per:
    if sum(pers) + p <= S:
        pers.append(p)

pers = pers[1:-1]

max_p = 0
for p in per:
    if p > pers[-1]:
        if sum(pers) + p <= S:
            max_p = max(max_p, p)

print(len(pers)+1, max_p)