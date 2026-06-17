with open(r'./files/17_29971.txt') as file:
    data = [int(i) for i in file]

max_data = max(n for n in data if abs(n) % 100 == 33)

ans = []
for nums in zip(data, data[1:], data[2:]):
    u = [len(str(abs(n))) == 2 for n in nums]
    summ = sum(nums)**2
    if sum(u) == 2 and summ < max_data:
        ans.append(sum(nums))

print(len(ans), max(ans))