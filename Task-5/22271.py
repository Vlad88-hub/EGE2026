def convert(num, sys):
    res = ''
    while num != 0:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for N in range(1, 100000):
    R = convert(N, 8)
    if R[0] == '5':
        R = R.replace('2', '!')
        R = R.replace('1', '2')
        R = R.replace('!', '1')
        R = '11' + R
    else:
        R = '2' + R[1:] + '10'
    R = int(R, 8)
    if R < 1354:
        ans.append([R, N])
print(max(ans))




# nt = 0
# while num:
#     if num % 125 <= 37:
#         cnt += 1
#     num //= 125
# print(cnt)