from re import *

with open(r'../files/24_17641.txt') as file:
    data = file.readline()

dat = '123+345*32+1+0*34++832+8'

num = r'([1-9][0-9]*|0)'
prod= fr'({num}\*)*0(\*{num})*'
pattern = fr'({prod}\+)+{prod}'

matches = [match.group() for match in finditer(pattern, data)]

print(len(max(matches, key=len)))