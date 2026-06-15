with open(r'./files/14250.txt') as file:
    data = [list(map(int, i.split())) for i in file]

summ = 0
for pos, nums in enumerate(data, start=1):
    u = len(nums) == len(set(nums))
    dif_3 = (max(nums) - min(nums))**3
    sum_2 = (sum(nums) - max(nums) - min(nums))**2
    if  u and dif_3 >= sum_2:
        summ += pos

print(summ)