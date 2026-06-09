num = 2*2401**525 + 3*343**524 - 4*49**523 + 5*49**522 - 6*7**521 - 35
print(num)
cnt_9 = 0
while num:
    if num % 49 <= 9:
        cnt_9 += 1
    num //= 49

print(cnt_9)