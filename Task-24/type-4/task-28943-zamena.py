with open(r'../files/24_28943.txt') as file:
    data = file.readline()

data = data.split('20')
for i in 'AEIUYO':
    data = data.relace(i, '*')

ans = 10*10
for i in range(len(data) - 24):
    line = '20' + '20'.join(data[i:i+25]) + '20'
    line_end = data[i+25]
    # if line_end:
    #     while line[0] not in 'AEIOUY':

