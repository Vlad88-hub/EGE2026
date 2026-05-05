from itertools import combinations

with open(r'../files/24_7600.txt') as file:
    data = file.readline()

data = data.replace('QR', 'Q R')
data = data.replace('RQ', 'R Q')
data = data.replace('QS', 'Q S')
data = data.replace('SQ', 'S Q')
data = data.replace('QQ', 'Q Q')
data = data.replace('QQ', 'Q Q')
data = data.replace('RS', 'R S')
data = data.replace('SR', 'S R')
data = data.replace('RS', 'R S')
data = data.replace('RR', 'R R')
data = data.replace('SS', 'S S')

data = data.split()

print(len(max(data, key=len)))

#################################################################################

# alph = 'ORS'
# # print(*combinations(alph, 2))
# for i in combinations(alph, 2):
#     i1 =  ''.join(i)
#     data = data.replace(i1, '* *')
#     data = data.replace(i1[::-1], '* *')
#
# data = data.replace('SS', 'S S')
# data = data.replace('RR', 'R R')
# data = data.replace('QQ', 'Q Q')
#
# data = data.split()
#
# print(len(max(data, key=len)))