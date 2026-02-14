from re import *

with open(r'.\files\24_25361.txt') as file:
    data = file.readline()

pattern = r'[02468]([^2468F]*F){76}[^2468F]*'
matches = [match.group() for match in finditer(pattern, data)]

print(len(max(matches, key=len)))