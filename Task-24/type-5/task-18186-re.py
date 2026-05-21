from re import finditer

with open(r'../files/24_18186.txt') as file:
    data = file.readline()

S = r'[BCDFGH]'
G = r'[AE]'
pattern = rf'(?<={S}{S}{G}).*?(?={S}{S}{G})'

matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len))+6)