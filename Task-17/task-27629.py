with open(r'./files/17_27629.txt') as file:
    data = [int(i) for i in file]

max_data = max(n for n in data if abs(n) % 100 == 43 and len(str(abs(n))) == 4)**2

ans = []
for nums in zip(data, data[1:]):
    u = [len(str(abs(n))) == 4 for n in nums]
    summ = sum(nums)**2
    if sum(u) >0 and summ < max_data:
        ans.append(summ)

print(len(ans), max(ans))