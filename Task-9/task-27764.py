with open(r'./files/27764.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for nums in data:
    if len(nums) == len(set(nums)) and (max(nums) + min(nums))*2 == sum(nums) - max(nums) - min(nums):
        cnt += 1

print(cnt)