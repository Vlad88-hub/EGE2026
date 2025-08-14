# Псевдослучайные числа
from random import *

# randint() - генерирует одно число на заданном диапазоне
# возвращает int.
rnd1 = randint(1,100)
print(rnd1)

# random() - генерирует одно число от нуля до оного
# возвращает float.
rnd2 = random()
print(rnd2)

# choice() - выбирает один случайный элемент из последовательности
rnd3 = choice([0,4,5,6,'fgsf'])
print(rnd3)

# sample() - выбирает k случайных элементов из последовательности
rnd4 = sample([0,4,5,6,'fgsf'], 2)
print(rnd4)
