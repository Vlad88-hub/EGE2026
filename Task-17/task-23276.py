with open(r'./files/17_23276.txt') as file:
    data = [int(i) for i in file]

max_data = max(n for n in data if abs(n) % 100 == 25)

ans = []
for nums in zip(data, data[1:], data[2:]):
    u = [len(str(abs(n))) == 4 for n in nums]
    summ = sum(nums)
    if sum(u) <= 2 and summ <= max_data:
        ans.append(summ)

print(len(ans), max(ans))