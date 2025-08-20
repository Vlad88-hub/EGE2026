from random import *
num = randint(0,100)
print('сгенерированное число:', num)
num1 = num % 10
num /= 3 if num1 % 3 == 0 else 1/2
print(num)