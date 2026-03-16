with open(r'.\files\17_17558.txt') as file:
    data = [int(i) for i in file]

del_32 = sum([1 for i in data if i % 32 == 0])

ans = []
for i in range(len(data) - 1):
    u = [n < 0 for n in data[i: i + 2]]
    summ = sum(data[i:i+2])
    if sum(u) >= 1 and  summ < del_32:
        ans.append(summ)

print(len(ans), max(ans))