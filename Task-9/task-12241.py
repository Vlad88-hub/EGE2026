with open(r'./files/12241.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for nums in data:
    amount = [nums.count(n) for n in set(nums)]
    pov = [n for n in set(nums) if nums.count(n) != 1]
    ne_pov = [n for n in set(nums) if nums.count(n) == 1]
    if sorted(amount) == [1, 2, 2, 2] and (max(pov) + min(pov)) / 2 < ne_pov[0]:
        cnt += 1

print(cnt)