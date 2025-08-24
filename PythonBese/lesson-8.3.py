num = int(input())
x = 0
while num:
    num //= 10
    x += 1
print(x)


num = int(input())
z = 0
while num:
    z += num % 10
    num //= 10
print(z)