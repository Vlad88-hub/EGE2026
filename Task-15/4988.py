cnt = 0
for x in range(1, 1001):
    for A in range(1, 1001):
        B = 70 <= x <= 80
        if  (x % 12 == 0) and B and (x % A != 0):
            cnt += 1
print(cnt)


