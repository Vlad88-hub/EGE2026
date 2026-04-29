with open(r'./files/1_17.txt') as file:
    data = [int(i) for i in file]

min_data = min(i for i in data if i > 0 and i % 123 == 0)

cnt = 0
for nums in zip(data, data[1:]):
    if sum(nums) < min_data:
        cnt += 1

print(cnt)