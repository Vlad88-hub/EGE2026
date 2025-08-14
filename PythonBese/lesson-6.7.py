from random import *
num = random()
num *= 10000
num = int(num)
print(num)
num1 = num // 1000
num2 = num % 10
num3 = num % 100 // 10
num4 = num // 100 % 10
print(num1 + num2 + num3 + num4)
