from re import *

with open(r'.\files\24_18937.txt') as file:
    data = file.readline()

pattern = r'([2-5][02345]*|0)'
matches = [match.group() for match in finditer(pattern, data)]

print(len(max(matches, key=len)))