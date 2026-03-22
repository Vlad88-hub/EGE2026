with open(r'.\files\17_21903.txt') as file:
    data = [int(i) for i in file]

min_data = min([i for i in data if len(str(abs(i))) == 3 and abs(i) % 100 == 15])**2

ans = []
for nums in zip(data, data[1:], data[2:]):
    print(nums, type(nums))
    u = [n > 0 for n in nums]
    mult = min(nums) * max(nums)
    if (sum(u) == 3 or sum(u) == 0) and mult > min_data:
        ans.append(mult)

print(len(ans), min(ans))