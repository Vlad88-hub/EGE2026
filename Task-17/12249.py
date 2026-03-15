with open(r'.\files\17_12249.txt') as file:
    data = [int(i) for i in file]

max_data = []
for i in data:
    if str(i)[-1] == '3' and len(str(abs(i))) == 5:
        max_data.append(i)
data_max = max(max_data)

ans = []
cnt = 0
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    u1 = str(num1)[-1] == '3'
    u2 = str(num2)[-1] == '3'
    u3 = str(num3)[-1] == '3'
    summ = num1 + num2 + num3
    if (u1 or u2 or u3) and summ < data_max:
        cnt += 1
        ans += [summ]

print(cnt, max(ans))