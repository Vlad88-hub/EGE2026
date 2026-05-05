with open(r'../files/24_7624.txt') as file:
    data = file.readline()

data = data.replace('XY', 'X Y')
data = data.replace('YX', 'Y X')
data = data.replace('XZ', 'X Z')
data = data.replace('ZX', 'Z X')
data = data.replace('XX', 'X X')
# data = data.replace('QQ', 'Q Q')
data = data.replace('YZ', 'Y Z')
data = data.replace('ZY', 'Z Y')
# data = data.replace('RS', 'R S')
data = data.replace('ZZ', 'Z Z')
data = data.replace('YY', 'Y Y')

data = data.split()

print(len(max(data, key=len)))