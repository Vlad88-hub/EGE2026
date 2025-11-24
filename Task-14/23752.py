from string import printable as pr

def convert(num, sys):
    res = ''
    while num != 0:
        res += pr[num % sys]
        num //= sys
    return res[::-1]


num_10 = 2*2187**2020 + 729**2021 - 2*243**2022 + 81**2023 - 2*27**2024 - 6561
num_27 = convert(num_10, 27)

cnt = 0
for i in num_27:
    if i > '9':
        cnt += 1

print(cnt)

###############################################################

num_10 = 2*2187**2020 + 729**2021 - 2*243**2022 + 81**2023 - 2*27**2024 - 6561

cnt = 0
while num_10:
    if num_10 % 27 > 9:
        cnt += 1
    num_10 //= 27

print(cnt)

