num = int(input())
x = 1
while num:
    x *= num % 10
    num //= 10
print(x)

