from string import printable as pr

for x in pr[:20]:
    num1 = int(f'627{x}J8', 20)
    num2 = int(f'H45I{x}5HIJ', 20)
    num3 = int(f'4IDB49J{x}7', 20)
    num = num1 + num2 + num3
    if num % 19 == 0:
        print(x, num // 19)