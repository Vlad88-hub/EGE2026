with open(r'./files/task-9.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for nums in data:
    u1 = max(nums) < (sum(nums) - max(nums))
    u2 = nums[0]+nums[1] != nums[2]+nums[3] and nums[0]+nums[2] != nums[1]+nums[3] and nums[0]+nums[3] != nums[2]+nums[1]
    if u1 + u2 == 2:
        cnt += 1

print(cnt)