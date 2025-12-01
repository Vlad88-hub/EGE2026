num = 15*343**2031 + 7*49**1142 - 3*7**111 + 7**222 - 16809

cnt_1 = 0
cnt_2 = 0
while num != 0:
    if (num % 7) % 2 == 0:
        cnt_1 += 1
    else:
        cnt_2 += 1
    num //= 7

print(cnt_1 - cnt_2)
print(int('566622', 7))