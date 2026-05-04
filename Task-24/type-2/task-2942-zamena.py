with open(r'../files/24_2942.txt') as file:
    data = file.readline()

for i in ['AC', 'AB']:
    data = data.replace(i, '*')
# data = data.replace('AB', '*')
# data = data.replace('AC', '*')
for i in 'ABC':
    data = data.replace(i, ' ')
# data = data.replace('A', ' ')
# data = data.replace('C', ' ')
# data = data.replace('B', ' ')
data = data.split()

print(len(max(data, key=len)))

# cnt = 0
# ans = []
# for i in range(len(data)):
#     if data[i] == '*':
#         cnt += 1
#         for j in range(len(data[i+1:])):
#             if data[j] == '*':
#                 cnt += 1
#             else:
#                 ans.append(cnt)
#                 cnt = 0
#                 break
#
# print(max(ans))