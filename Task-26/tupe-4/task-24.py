with open(r'../files/26_24.txt') as file:
    S, N = map(int, file.readline().split())
    per = [int(i) for i in file]

per = sorted(per)

pers = [0]
for p in per:
    if sum(pers) + p <= S:
        pers += [p]

# print(sum(pers))
# print(S)
# print(len(pers))
pers = pers[1:-1]
# print(len(pers))

max_pers = 0
for p in per:
    if p > pers[-1]:
        if sum(pers) + p <= S:
            max_pers = max(max_pers, p)

print(len(pers)+1, max_pers)