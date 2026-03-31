with open(r'.\files\24347.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for line in data:
    max_data = line.count(max(line)) == 1
    u_start = line[0] != max(line) and line[0] != min(line) and line[-1] != max(line) and line[-1] != min(line)
    mult = 1
    for n in sorted(line)[-3:]:
        mult *= n
    u1 = mult % min(line) == 0
    print(max_data + u_start + u1)
    if (max_data + u1 + u_start) == 1:
        cnt += 1


print(cnt)
