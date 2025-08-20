num = int(input('введите трехзначное число: '))
num1 = num // 100 #  первый десяток
num2 = num // 10 % 10 #  второй десяток
num3 = num % 10 # третий десяток
print(num1, num2, num3)
if (num1 % 2 == 0 or num1 % 5 == 0) and (num2 % 2 ==  0 or num2 % 5 == 0) or (num1 % 2 == 0 or num1 % 5 == 0) and (num3 % 2 == 0 or num3 % 5 == 0) or (num2 % 2 == 0 or num2 % 5 == 0) and (num3 % 2 == 0 or num3 % 5 == 0 ):
    print(num)
else:
    print(num+1)