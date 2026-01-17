from re import *

with open(r'.\files\24_10105.txt') as file:
    data = file.readline()

pattern = r'(?<=T)[^T]*T[^T]*(?=T)'
matches = [match.group() for match in finditer(pattern, data)]

print(len(max(matches, key=len)))