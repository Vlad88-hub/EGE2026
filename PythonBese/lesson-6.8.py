from random import *
num = int(input('введите максимальное значения '))
num1 = randint(0,num)
num1 /= 9
num1 *= 1000
num1 = int(num1)
num1 /= 1000
print('ответ = ', num1 )