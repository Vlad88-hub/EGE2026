with open(r'./files/29341.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for nums in data:
    if max(nums) < sum(nums) - max(nums) and max(nums) + min(nums) != sum(nums) - max(nums) - min(nums):
        cnt += 1

print(cnt)