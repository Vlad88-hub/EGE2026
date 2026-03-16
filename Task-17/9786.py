with open(r'.\files\17_9786.txt') as file:
    data = [int(i) for i in file]

max_data = max([i for i in data if abs(i) % 100 == 25])

ans = []
for i in range(len(data) - 2):
   u = [1 for n in data[i: i + 3] if len(str(abs(n))) == 4]
   summ = sum(data[i:i + 3])
   if sum(u) <= 2 and summ <= max_data:
       ans.append(summ)

print(len(ans), max(ans))