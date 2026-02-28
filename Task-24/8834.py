from re import *
# неправильно
with open(r'.\files\24-371.txt') as file:
    data = file.readline()


# data = data.replace(' ', '')
# data = data.replace('.', '. ')
# data = data.split()
#
# ans = 10**20
# for line in data:
#     if line.count('A') == 98 and line[-1] == '.':
#         ans = min(ans, len(line))
#
# print(ans)
########################################################################


pattern = r'(A[B-Z ]*){98}\.'
matches = [match.group() for match in finditer(pattern, data)]
print(len(min(matches, key=len)))