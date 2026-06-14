with open(r'./files/17_21903.txt') as file:
    data = [int(i) for i in file]

min_data = min(n for n in data if len(str(abs(n))) == 3 and abs(n) % 100 == 15)**2

ans = []
for nums in zip(data, data[1:], data[2:]):
    u = [n > 0 and n != 0 for n in nums]
    summ = max(nums) * min(nums)
    if (sum(u) == 3 or sum(u) == 0) and summ > min_data:
        ans.append(summ)

print(len(ans), min(ans))