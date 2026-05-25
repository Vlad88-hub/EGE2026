from re import *

with open(r'../files/24_28943.txt') as file:
    data = file.readline()

dat = '*****20****20E***20****20**A*****20***2020***Y'

data = data.replace('20', '!')
pattern = r'(![^!AEIOUY]*){26}[AEIOUY]'
matches = [match.group() for match in finditer(pattern, data)]
# print(matches)

print(len(min(matches, key=len).replace('!', '20')))