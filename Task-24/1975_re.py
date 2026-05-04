from platform import machine
from re import *

with open(r'.\files\24_1975.txt') as file:
    data = file.readline()

pattern = r'[^P]*(P[^P]+)+[P]?'
pattern_2 = 'P?([^P]+P)+[^P]*'
matches = [match.group() for match in finditer(pattern_2, data)]
print(len(max(matches, key=len)))