from random import *
num = int(input('введите трехзначное число '))
num1 = randint(100,999)
if num // 1000 == 0 and num // 100 != 0:
    print('введеное число:', num)
    print('сгенерированное число:', num1)
    print('введенное число больше ' if num > num1 else 'введенное число меньше ')
else:
    print('число:', num, 'не трехзначное')

