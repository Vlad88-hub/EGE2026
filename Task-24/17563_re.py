from re import *

with open(r'.\files\24_17563.txt') as file:
    data = file.readline()

pattern = r'[1-9][0-9]*([-\*][1-9][0-9]*)*'
mathces = [match.group() for match in finditer(pattern, data)]
print(len(max(mathces, key=len)))