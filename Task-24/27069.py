from re import *

with open(r'.\files\24_27069.txt') as file:
    data = file.readline()

word = r'([A-Z][a-z]*|[a-z]+)'
pattern = fr'[A-Z][a-z]*({word})+\.'
matches = [match.group() for match in finditer(pattern, data)]

print(max( matches, key=len))