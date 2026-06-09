with open(r'./files/17_23376.txt') as file:
    data = [int(i) for i in file]

max_data = max(n for n in data if len(str(abs(n))) == 5 and abs(n) % 100 == 37)**2

ans = []
for nums in zip(data, data[1:]):
    u = [len(str(abs(n))) == 5 for n in nums]
    sum_nums = sum(nums)
    if sum(u) == 1 and sum_nums**2 > max_data:
        ans.append(sum_nums)

print(len(ans), max(ans))

