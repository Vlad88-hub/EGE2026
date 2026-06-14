with open(r'./files/17_21416.txt') as file:
    data = [int(i) for i in file]

sum_neg = sum(n for n in data if n < 0)

ans = []
for nums in zip(data, data[1:], data[2:]):
    prod = max(nums) * min(nums)
    if prod > sum_neg:
        ans.append(sum(nums))

print(len(ans), max(ans))