with open(r'.\files\17_6791.txt') as file:
    data = [int(i) for i in file]


min_data = min([n for n in data if abs(n) % 100 == 68])**2

ans = []
for nums in zip(data, data[1:]):
    u = [abs(n) % 100 == 68 for n in nums]
    u2 = nums[0]**2 + nums[1]**2 >= min_data
    if sum(u) == 1 and u2:
        ans.append(nums[0]**2 + nums[1]**2)

print(len(ans), max(ans))