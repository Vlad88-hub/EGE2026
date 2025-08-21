# >, <, >=, <=, ==, !=, not, and, or

# цикл

# while - работает, пока выполняется условие

# num = 10
# while num >= 5:
#     print(num)
#     num -= 1

# continue - оператор перехода цикла на следующий шаг
# num = 10
# while num >= 5:
#     num -= 1
#     if num % 2 == 0:
#         continue
#     print(num)

# break - оператор прекращения работы цикла

# num = 10
# while num >= 5:
#     num -= 1
#     if num == 7:
#         break
#     print(num)

from random import *
# while True:
#     num = randint(0,1000)
#     if num % 2 == 0:
#         break
#      print(num)

# else - выполняет блок кода, если цикл завершится без break
# num = 0
# while num < 3:
#     ran = randint(0,100)
#     if ran % 2 == 0:
#         break
#     print(ran)
#     num += 1
# else:
#     print('все числа нечетные')

# Считать с клавиатуры число любой длины.
# Вывести на экран все цифры числа при помощи цикла While.

# num = int(input())
# while num: # пока число существует или не превратилось в 0
#     print(num % 10)
#     num //= 10

# цил for - выполняет N-е количество шагов
# for i in <итерируемый объект или последовательность>
# data = 'hello'
# for i in data:
#     print(i)

# range(start, stop, step) - генерирует диапазон от start до stop  не включительно с шага step

# for i in range(2): # -> 0, 1
#     print('hi', i)

# for i in range(5,8): # -> 5, 6, 7
#         print('hi', i)

# for i in range(10, 5, -1):  # -> 10, 9, 8, 7, 6
#             print('hi', i)

for i in range(9, 6, -1):
            print('hi', i)