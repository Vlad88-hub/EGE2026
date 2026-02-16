def summ(num):
    for a in range(113, 10**6, 113*2):
        for x in range(1, 13):
            if a + 3 ** x == num:
                return x
    return 0


cnt = 0
for n in range(111111, 1000000):
    F = summ(n)
    if str(n).count('0') == 0 and F:
        print(n, F)
        cnt += 1
        if cnt == 5:
            break