with open(r'.\files\17_2997.txt') as file:
    data = [int(i) for i in file]

nums_3 = [int(str(abs(i))[1]) for i in data if len(str(abs(i))) == 3]
most_common = max((nums_3.count(i), i) for i in range(10))[1]

ans = []
for nums in zip(data, data[1:]):
    if any([abs(n) % 10 == most_common for n in nums]):
        ans += [sum(nums)]

print(len(ans), max(ans))
