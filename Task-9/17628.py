with open(r'.\files\17628.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for line in data:
    summ = max(line) + min(line)
    all_sum = sum(line) - summ
    if summ <= all_sum:
        cnt += 1

print(cnt)