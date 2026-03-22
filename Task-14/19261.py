def convert_new(num, sys):
    num = num[::-1]
    # print(num)
    res = 0
    for i in range(len(num)):
        res +=  num[i] * sys**i
    return res

ans = []
for x in range(1, 37):
    num1 = convert_new([9, 8, x, 3, 1], 37)
    num2 = convert_new([1, x, 9, 2, 4], 37)
    num = num1 + num2
    if num % 21 == 0:
        ans.append([x, num // 21])

print(max(ans))


# print(convert_new([9, 8, 36, 3, 1], 37))
# print(int('A', 30))
# # num = '12382'
# print(num.index('1'))