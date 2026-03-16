with open(r'.\files\17_17636.txt') as file:
    data = [int(i) for i in file]

max_data = max([i for i in data if abs(i) % 10 == 3 and len(str(abs(i))) == 3])

ans = []
for i in range(len(data) - 2):
    u = [abs(n) % 10 == 3 and len(str(abs(n))) == 3 for n in data[i: i + 3]]
    summ = sum(data[i: i + 3])
    if sum(u) >= 1 and summ < max_data:
        ans += [summ]

print(len(ans), max(ans))