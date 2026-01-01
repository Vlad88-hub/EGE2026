from string import *
with open(r'.\files\24_4642.txt') as file:
    data = file.readline()

for i in ascii_uppercase:
    data = data.replace(i, '!')

for i in digits:
    data = data.replace(i, '-')

data = data.replace('!-', '*')

for i in '!-':
    data = data.replace(i, ' ')

data = data.split()
print(len(max(data, key=len)))