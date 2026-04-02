with open(r'.\files\26.txt') as file:
    N = file.readline()
    data = [list(map(int, i.split())) for i in file]

data =sorted(data)

check = set()
for i in data:
    check |= {i[1]}

ans = []
for i in check:
    sport = []
    cnt_sport = 0
    for n in data:
        if n[1] == i:
            cnt_sport += 1
            sport += [n[0]]
    cnt = 0
    sport = set(sport)
    for p in range(len(sport)):
        if sport[p+1] - sport[p] == 1:
            cnt += 1
    if len(sport) - cnt == 1:
        ans.append([len(sport), i])

print(max(ans))