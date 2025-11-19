from string import printable as pr

def convert(num, sys):
    res = ''
    while num != 0:
        res += pr[num % sys]
        num //= sys
    return res[::-1]

num1 = 41
num2 = 131

print(convert(num1, 2))
print(convert(num2, 2))

print(convert(num1, 3))
print(convert(num2, 3))

print(convert(num1, 4))
print(convert(num2, 4))

print(convert(num1, 5))
print(convert(num2, 5))

print(convert(num1, 6))
print(convert(num2, 6))

print(convert(num1, 7))
print(convert(num2, 7))

print(convert(num1, 8))
print(convert(num2, 8))

print(convert(num1, 9))
print(convert(num2, 9))

print(convert(num1, 10))
print(convert(num2, 10))

print(convert(num1, 11))
print(convert(num2, 11))

print(convert(num1, 12))
print(convert(num2, 12))

print(convert(num1, 13))
print(convert(num2, 13))
