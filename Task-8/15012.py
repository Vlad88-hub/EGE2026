from itertools import product
from string import printable as pr

cnt  = 0
for val in product(pr[:14], repeat=5):
    val = ''.join(val)
    if val[0] != '0' and (val[-1] == '3' or val[-1] == '0'):
        if len(set(val)) == 2:
            cnt += 1



#         cnt_ne3 = 0
#         for i in val:
#             if i != '3':
#                 cnt_ne3 += 1
#         if cnt_ne3 == 1:
#             print(val)
#             ans += 1
#
#         cnt_0 = 0
#
#         for i in val:
#             if i != '0':
#                 cnt_0 += 1
#         if cnt_0 == 1:
#             ans += 1
print(cnt)
