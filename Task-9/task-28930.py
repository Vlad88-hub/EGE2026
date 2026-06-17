with open(r'./files/28930.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for nums in data:
    cnt_2 = 0
    for i in range(len(nums) - 1):
        if nums[i + 1] > nums[i]:
            cnt_2 += 1
    if cnt_2 == 4 and max(nums) + min(nums) <= sum(nums) - max(nums) - min(nums):
        cnt +=1

print(cnt)