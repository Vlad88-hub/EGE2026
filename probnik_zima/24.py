from re import *

with open(r'..\Task-24\files\24.txt') as file:
    data = file.readline()

pattern = r'(0|[789][0789]*)([-\*](0|[789][0789]*))+'
matches = [match.group() for match in finditer(pattern, data)]

print(len(max(matches, key=len)))