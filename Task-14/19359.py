from string import printable as pr

ans = []
for x in pr[:22]:
    num1 = int(f'a23{x}ac0', 22)
    num2 = int(f'gb{x}21670', 22)
    num = num1 + num2
    if num % 21 == 0:
        ans.append([x, num // 22])
print(max(ans))
