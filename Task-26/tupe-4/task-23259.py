with open(r'../files/26_15_23259.txt') as file:
    N, M = map(int, file.readline().split())
    exp = [int(file.readline()) for i in range(N)]
    san = [int(file.readline()) for j in range(M)]

exp = sorted(exp)
san = sorted(san)

last_san = 0
exp_2 = []
for e in exp:
    for s in san:
        if s >= e:
            last_san = s
            exp_2.append(e)
            san.remove(s)
            break

exp_2 = exp_2[:-1]
for e in exp[::-1]:
    if last_san >= e:
        exp_2.append(e)
        break

print(len(exp_2), exp_2[-1])

