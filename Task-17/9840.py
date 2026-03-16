with open(r'.\files\17_9840.txt') as file:
    data = [int(i) for i in file]

max_data = max([i for i in data if len(str(abs(i))) == 4 and i % 100 == 39])

ans = []
for i in range(len(data) - 1):
    u = [len(str(abs(n))) == 4 for n in data[i: i + 2]]
    summ = sum(data[i: i + 2])
    if sum(u) == 1 and summ**2 <= max_data**2:
        ans.append(summ)

print(len(ans), max(ans))