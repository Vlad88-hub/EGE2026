from itertools import *

cnt = 0
for val in product('полина', repeat=8):
     val = ''.join(val)
     for i in 'плн':
         val = val.replace(i, '!')
     for i in 'оиа':
         val = val.replace(i, '@')
     if val.count('!') > val.count('@'):
         cnt += 1
print(cnt)

# cnt = 0
# for val in product('полина', repeat=8):
#     val = ''.join(val)
#     if val.count('п') + val.count('л') + val.count('н') > val.count('0') + val.count('и') + val.count('а'):
#         cnt += 1
# print(cnt)
print(19+16+14+12+10+8+7+5+4+3+2+1+1)