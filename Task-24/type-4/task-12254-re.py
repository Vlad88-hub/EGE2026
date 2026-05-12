from re import *

with open(r'../files/24_12254.txt') as file:
    data = file.readline()

pattern = r'(SQ|Q)?(RSQ)+(RS|R)?'
matches = [match.group() for match in finditer(pattern, data)]

print(len(max(matches, key=len)))