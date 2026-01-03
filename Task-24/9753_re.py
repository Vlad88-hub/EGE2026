from re import *

with open(r'.\files\24_9753.txt') as file:
    data = file.readline()

pattern = r'(^|(?=<Y))([^Y]*Y){150}[*Y]*($|(*=Y))'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))