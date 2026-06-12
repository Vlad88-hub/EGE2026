with open(r'./files/17_17558.txt') as file:
    data = [int(i) for i in file]

sum_32 = sum(abs(n) % 32 == 0 for n in data)

ans = []
for nums in zip(data, data[1:]):
    u = [n < 0 for n in nums]
    summ = sum(nums)
    if sum(u) >= 1 and summ < sum_32:
        ans.append(summ)

print(len(ans), max(ans))