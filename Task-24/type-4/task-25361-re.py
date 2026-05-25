from re import *

with open(r'../files/24_25361.txt') as file:
    data = file.readline()

dat = '***8f**f***f*8f***ffff'

pattern = r'[02468]([^F02468]*F){76}[^F02468]*'
matches = [match.group() for match in finditer(pattern, data)]

print(len(max(matches, key=len)))