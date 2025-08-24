num = int(input()) # 202, 220, 222
x = 1
if num % 10 != 0 and num // 10 % 10 != 0:
    while num:
        x *= num % 10
        num //= 10
else:
    x -= 1
    while num:
        x += num % 10
        num //= 10
print(x)



