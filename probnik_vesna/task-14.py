ans = []
for x in range(1, 9431):
    cnt_0 = 0
    num = 39**483 + 39**235 - x
    while num:
        if num % 39 == 0:
            cnt_0 += 1
        num //= 39
    ans.append(cnt_0)

print(max(ans))