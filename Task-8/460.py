from itertools import product as pr

d = set()
for val in pr('01234', repeat=5):
    val = ''.join(val)
    for min_val in pr('01234', repeat=5):
        min_val = ''.join(min_val)
        if val[0] != '0' and min_val[0] != '0' and int(val, 5) > int(min_val, 5):
            d |= {int(val, 5) - int(min_val, 5)}

print(len(d))