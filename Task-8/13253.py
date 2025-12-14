from itertools import product as pr

cnt_1 = 0
cnt_2 = 0
for val in pr('конец', repeat=5):
    val = ''.join(val)
    if val.count('е') >= 1 or val.count('ц') >= 1:
        cnt_1 += 1

for val_2 in pr('дракон', repeat=5):
    val_2 = ''.join(val_2)
    if val_2.count('д') >= 1 or val_2.count('р') >= 1 or val_2.count('а') >=1:
        cnt_2 += 1

print(cnt_1 + cnt_2)