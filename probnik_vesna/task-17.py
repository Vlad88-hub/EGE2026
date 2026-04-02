with open(r'.\files\17.txt') as file:
    data = [int(i) for i in file]

max_data = max([i for i in data if len(str(i)) == 2])

ans = []
for nums in zip(data, data[1:]):
    u = [len(str(n)) == 2 for n in nums]
    u2 = sum(nums) % max_data == 0
    if sum(u) == 1  and u2:
        ans.append(sum(nums))

print(len(ans), max(ans))