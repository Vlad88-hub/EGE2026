num = int(input())
x = 0
while num:
    num1 = num % 10
    if num1 % 2 == 0:
        x += 1
    num //= 10
print(x)