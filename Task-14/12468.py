from string import printable as pr

ans = []
for x in pr[:19]:
    num1 = int(f'78{x}79643', 19)
    num2 = int(f'25{x}43', 19)
    num3 = int(f'63{x}5', 19)
    num = num1 + num2 + num3
    if num % 18 == 0:
        ans.append([x, num // 18])
print(min(ans))