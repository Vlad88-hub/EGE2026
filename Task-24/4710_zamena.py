from string import *
with open(r'.\files\24_4710.txt') as file:
    data = file.readline()

vow = 'AO'
for i in ascii_uppercase:
    if i in vow:
        data = data.replace(i, '!')

    else:
        data = data.replace(i, '@')


data = data.replace('!@', '*')
data = data.replace('!', ' ')
data = data.replace('@', ' ')

data = data.split()

print(len(max(data, key=len)))