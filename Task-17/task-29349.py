with open(r'./files/17_29349.txt') as file:
    data = [int(i) for i in file]

min_data = min(n for n in data if n > 0 and abs(n) % 123 == 0)

ans = []
for nums in zip(data, data[1:]):
    summ = sum(nums)
    if summ < min_data:
        ans.append(summ)

print(len(ans), max(ans))