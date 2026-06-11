with open(r'./files/17_16383.txt') as file:
    data = [int(i) for i in file]

max_data = max(n for n in data if len(str(abs(n))) == 5 and abs(n) % 100 == 21)**2

max_sum = []
for nums in zip(data, data[1:]):
    u = [len(str(abs(n))) == 5 and abs(n) % 100 == 21 for n in nums]
    summ = sum(n**2 for n in nums)
    if sum(u) == 1 and summ >= max_data:
        max_sum.append(sum(nums))

print(len(max_sum), max(max_sum))