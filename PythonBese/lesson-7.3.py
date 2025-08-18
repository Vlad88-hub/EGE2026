from random import *
num = randint(0,100)
print(num)
num /= 3 if num % 3 == 0 else 1/2 # тернарник
print(num)