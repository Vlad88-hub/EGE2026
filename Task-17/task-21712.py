with open(r'./files/17_21712.txt') as file:
    data = [int(i) for i in file]

min_data = min(n for n in data if n > 0 and len(str(n)) == 4 and n % 10 == 6)

ans = []
for nums in zip(data, data[1:], data[2:]):
    u = [len(str(abs(n))) == 4 and abs(n) % 10 == 6 for n in nums]
    summ = sum(nums)
    if sum(u) == 1 and summ <= min_data:
        ans.append(summ)

print(len(ans), max(ans))