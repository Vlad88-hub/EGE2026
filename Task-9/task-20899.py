with open(r'./files/20899.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for nums in data:
    amount = [nums.count(n) for n in set(nums)]
    if sorted(amount) == [1,1,2] and max(nums) < sum(nums) - max(nums):
        cnt += 1

print(cnt)