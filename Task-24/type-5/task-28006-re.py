from re import *

with open(r'../files/24_28006.txt') as file:
    data = file.readline()

dat = '1232()12(122+7)(8-721)(21-0)(78'
num = r'\(([1-9][0-9]*[024689]|[02468])[+-]([1-9][0-9]*[13579]|[13579])\)'

pattern = fr'({num})*'
matches = [match.group() for match in finditer(pattern, data)]
# print(matches)
print(len(max(matches, key=len)))