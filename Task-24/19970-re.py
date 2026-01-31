from re import *

with open(r'.\files\24_19970.txt') as file:
    data = file.readline()

pattern = r'(0|5|[1-9][0-9]*[05])([+\*](0|5|[1-9][0-9]*[05]))+'
matches = [match.group() for match in finditer(pattern, data)]

print(len(max(matches, key=len)))