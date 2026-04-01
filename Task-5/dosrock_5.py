ans = []
for N in range(1, 100000):
    R = bin(N)[2:]
    if N % 3 == 0:
        R += R[-3:]
    else:
        R += bin((N % 3 )* 3)[2:]

    R = int(R, 2)
    if R >= 200:
        ans.append(N)

print(min(ans))


# data ='123456'
# print(data[-3:])