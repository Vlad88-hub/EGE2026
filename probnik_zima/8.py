from itertools import product, repeat
from string import printable as pr

netch = '13579bdfhjln'
ans = 0
for val in product(pr[:25], repeat=4):
    val = ''.join(val)
    if val[0] != '0':
        if (val[0] in netch and val[1] not in netch and val[2] not in netch and val[3] not in netch) or (val[0] not in netch and val[1] in netch and val[2] not in netch and val[3] not in netch) or (val[0] not in netch and val[1] not in netch and val[2] in netch and val[3] not in netch) or (val[0] not in netch and val[1] not in netch and val[2] not in netch and val[3]  in netch):
            cnt = 0
            for p in val:
                if int(p, 25) >= 5:
                    cnt += 1
                    if cnt <= 2:
                        ans += 1

print(ans)