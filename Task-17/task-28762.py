with open(r'./files/17_28762.txt') as file:
    data = [int(i) for i in file]

min_data = min(n for n in data if n % 23 == 0)

ans = []
for nums in zip(data, data[1:]):
    u = [n % min_data == 0 for n in nums]
    if sum(u) > 0:
        ans.append(sum(nums))

print(len(ans), max(ans))