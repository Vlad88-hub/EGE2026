from re import finditer
from string import printable

with open(r'../files/24_22356 (1).txt') as file:
    data = file.readline()

pattern = r'[1-9AB][0-9AB]*[13579B]'
matches = [[match.group(), match.start()] for match in finditer(pattern, data)]

print(max(matches, key=lambda x: int(x[0], 12))[1])

##############################################################3

# max_len = 0
# pos_i = 0
# for i in range(len(data)):
#     if data[i] in printable[1:12]:
#         cnt = 1
#         for j in range(i+1, len(data)):
#             if data[j] in printable[:12]:
#                 cnt += 1
#             elif data[j- 1] in printable[1:12:2]:
#                 if cnt > max_len:
#                     max_len = cnt
#                     pos_i = i
#                     break
#             else:
#                 break
# print(pos_i)
