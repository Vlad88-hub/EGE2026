# системы счисления

# двоичная система
n = 25
# bin() - переводит число в двоичную систему из десятичной
# принимает на вход int, возвращает str
print(bin(n))
# [2:] - срез убирающий первые два символа '0b'
print(bin(n)[2:])
# f'' - форматируемая строка, которая позволяет в себя переменные
print(f'{n:b}')

# восьмеричная система
# oct - переводит число в восьмеричную систему счисления из десятичной
# принимает на вход int, возвращает str
print(oct(n)[2:])
print(f'{n:o}')

# шестнадцатеричная система
# hex - переводит число в шестнадцатеричную систему из десятичной
# принимает на вход int, возвращает str
print(hex(n)[2:])
print(f'{n:x}')

# перевод в любую систему счисления (2 <== sys <== 9)
def convert(num, sys):
    res = ''
    while num != 0:
        res += str(num % sys)
        num //= sys
    return res[:: -1]

print(convert(31, 3))

# перевод в любую систему счисления (2 <== sys <== 36)
from string import printable

def convert2(num, sys):
    res = ''
    while num != 0:
        res += printable[num % sys]
        num //= sys
    return res[:: -1]

print((convert2(16*15+1, 16)))

# Перевод в десятичную систему
num_bin = '1010'
num_tri = '102'
num_hex = 'af8'
print(int(num_bin, 2))
print(int(num_tri, 3))
print(int(num_hex, 16))

# срезы
test = 'Hello world!'
# извлечение первых двух символов
print(test[:2])
# строка без первых двух символов
print(test[2:])
# извлечение последних двух символов
print(test[-2:])
# строка без последних двух символов
print(test[:-2])

# .append -> сохранание в список

# сумма цифр числа
# двоичное число
num_1 = '1010'
print(num_1.count('1'))

# системы до 10 включительно
num_2 = '823'
print(sum(map(int, num_2)))

# системы до 36 включительно
num_3 = 'AF5'
print(sum(map(lambda x: int(x, 36), num_3)))