from math import prod
with open(r'.\files\17_11236.txt') as file:
    data = [int(i) for i in file]

min_data = min([i for i in data if len(str(abs(i))) == 2])
max_data = max([i for i in data if len(str(abs(i))) == 4 and abs(i) % 10 == 1])

ans = []
for i in range(len(data) - 2):
    u1 = sum([n > min_data**2 for n in data[i:i+ 3]]) == 2
    u2 = prod(map(abs, data[i:i + 3])) % abs(max_data) == 0
    if u1 and u2:
        ans += [sum(map(abs, data[i:i + 3]))]

print(len(ans), max(ans))