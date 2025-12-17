from re import *

with open(r'.\files\24_1866.txt') as file:
    data = file.readline()
pattern = r'(?<=(ad|da)).+?(?=(ad|da))'
matches = [match.group() for match in finditer(pattern, data)]

print(len(max(matches, key=len)) + 2)
# max_str = max(matches, key=len)
# ans_len = len(max_str)
# if data.find(max_str) == 0:
#     ans_len += 1
# elif data.rfind(max_str) == len(data) - ans_len:
#     ans_len += 1
# else:
#     ans_len += 2


