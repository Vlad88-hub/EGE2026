from string import *
with open(r'.\files\24_21421.txt') as file:
    data = file.readline()

alph = '0123456789AB'
alph_chet = '02468A'
for i in ascii_uppercase + digits:
    if i not in alph:
        data = data.replace(i, ' ')

data = data.split()
ans = 0
for num in data:
    num = num.lstrip('0')
    if num and num [-1] in alph_chet:
        ans = max(ans, len(num))
    else:
        while num and num[-1] not in alph_chet:
            num = num[:-1]
        if num:
            ans = max(ans, len(num))
print(ans)