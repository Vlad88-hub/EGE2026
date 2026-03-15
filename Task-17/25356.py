with open(r'.\files\17_25356.txt') as file:
    data = [int(i) for i in file]

max_data = 0
for i in data:
    if i % 100 == 30:
        max_data = max(i, max_data)

ans = []
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    u1 = len(str(abs(num1))) != 4
    u2 = len(str(abs(num2))) != 4
    u3 = len(str(abs(num3))) != 4
    summ = num1 + num2 + num3
    if all((u1, u2, u3)) and summ > max_data:
        ans += [summ]

print(len(ans), max(ans))