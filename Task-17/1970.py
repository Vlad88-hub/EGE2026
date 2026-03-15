with open(r'.\files\17_1970.txt') as file:
    data = [int(i) for i in file]

ans = []
cnt = 0
for num1, num2 in zip(data, data[1:]):
    u1 = num1 % 3 == 0
    u2 = num2 % 3 == 0
    if u1 or u2:
        cnt += 1
        ans.append(num1 + num2)

print(cnt, max(ans))