from string import printable as pr

ans = []
for x in pr[:25]:
    num1 = int(f'11353{x}12', 25)
    num2 = int(f'135{x}21', 25)
    num = num1 + num2
    if num % 24 == 0:
        ans.append([x, num // 24])
print(max(ans))
