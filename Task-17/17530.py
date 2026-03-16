with open(r'.\files\17_17530.txt') as file:
    data = [int(i) for i in file]

min_data = sorted(data)[0]

ans = []
for num1, num2 in zip(data, data[1:]):
    u1 = num1 % 55 == min_data
    u2 = num2 % 55 == min_data
    if u1 + u2 >= 1:
        ans.append(num1 + num2)

print(len(ans), min(ans))