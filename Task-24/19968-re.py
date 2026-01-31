from re import *

with open(r'.\files\24_19968.txt') as file:
    data = file.readline()

pattern = r'([1-5][0-5]*|0)([+\*]([1-5][0-5]*|0))+'
matches = [match.group() for match in finditer(pattern, data)]

print(len(max(matches, key=len)))