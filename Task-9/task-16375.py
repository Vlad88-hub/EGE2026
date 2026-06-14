with open(r'./files/16375.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for nums in data:
    amount = [nums.count(n) for n in set(nums)]
    pov = [n for n in set(nums) if nums.count(n) != 1]
    ne_pov = sorted([n for n in set(nums) if nums.count(n) == 1])
    if sorted(amount) == [1, 1, 1, 1, 1, 2] and ne_pov[0] * ne_pov[1] * ne_pov[2] > pov[0] ** 2:
        cnt += 1

print(cnt)