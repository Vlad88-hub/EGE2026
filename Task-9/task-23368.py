with open(r'./files/23368_2.txt') as file:
    data = [list(map(int, i.split())) for i in file]

for pos, nums in enumerate(data, start=1):
    amount = [nums.count(n) for n in set(nums)]
    summ = max(nums) + min(nums)
    # print(nums)
    if len(amount) == 5 and summ*2 == (sum(nums) - summ)*3:
        print(pos)