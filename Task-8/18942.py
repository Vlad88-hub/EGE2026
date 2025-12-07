from itertools import *

cnt = 0
cnt_2 = 0
for val in product('доинсй', repeat=6):
    val = ''.join(val)
    if val.count('д') == 0 and 'оо' not in val and 'ии' not in val and 'нн' not in val and 'сс' not in val and 'йй' not in val and val.count('н') >= 1:
        cnt += 1
        print(val)
    elif val.count('н') == 0 and 'оо' not in val and 'ии' not in val and 'дд' not in val and 'сс' not in val and 'йй' not in val and val.count('д') >= 1:
        cnt_2 += 1
print(cnt + cnt_2)

