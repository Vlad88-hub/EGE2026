with open(r'files/17968.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for line in data:
    u1 = max(line) < sum(line) - max(line)
    u2 = sum([n for n in line if n % 2 == 0]) == sum([n for n in line if n % 2 != 0])
    if u2 and u1:
        cnt += 1

print(cnt)