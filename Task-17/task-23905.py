with open(r'./files/17_23905.txt') as file:
    data = [int(i) for i in file]

max_data = max(n for n in data if n % 100 == 37)

ans = []
for nums in zip(data, data[1:], data[2:], data[3:]):
    u1 = []
    for n in nums:
        if len(str(n)) >= 2:
            if str(n)[-1] == str(n)[-2]:
                u1.append(n)
    u2 = [n > max_data for n in nums]
    if len(u1) == 1 and sum(u2) == 2:
        ans.append(u1[0])

print(len(ans), sum(ans))

# dat = '12263'
# print(dat[-2])
# n for n in nums if str(n)[-1] == str(n)[-2]