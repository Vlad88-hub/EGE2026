with open(r'./files/22547.txt') as file:
    data = [list(map(int, i.split())) for i in file]

ans = []
for pos, nums in enumerate(data, start=1):
    chet = [n % 2 == 0 for n in nums]
    ne_chet = [n % 2 != 0 for n in nums]
    u = [n2 > n1 for n1, n2 in zip(nums, nums[1:])]
    if sum(chet) == sum(ne_chet) and sum(u) == 5:
        print(pos, sum(nums))
