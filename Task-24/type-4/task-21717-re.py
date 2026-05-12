from re import *

with open(r'../files/24_21717.txt') as file:
    data = file.readline()

pattern = r'RSQ([FGQRS]*RSQ){129}[^Q]'
matches = [match.group() for match in finditer(pattern, data)]

print(len(min(matches, key=len)))