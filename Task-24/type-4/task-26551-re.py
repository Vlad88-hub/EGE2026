from re import *

with open(r'../files/24_26551.txt') as file:
    data = file.readline()

pattern = r'[1-9A-D][0-9A-D]*[2468AC]'
matches = [match.group() for match in finditer(pattern, data)]

print(len(max(matches, key=lambda x: int(x, 14))))