with open(r'./files/17_28938.txt') as file:
    data = [int(i) for i in file]

max_data = max(n for n in data if abs(n) % 100 == 28)

ans = []
for nums in zip(data, data[1:], data[2:]):
    u = [len(str(abs(n))) == 3 for n in nums]
    srd = sum(nums) / 3
    u2 = srd >0
    if sum(u) >= 1 and srd < max_data and u2:
        ans.append(sum(nums))

print(len(ans), max(ans))