with open(r'../files/26_6641.txt') as file:
    N, M = map(int, file.readline().split())
    prod = [list(map(int, i.replace('S', '0').replace('W', '1').split())) for i in file]

prod = sorted(prod)
sum_prod = []
summ = 0
for p in prod:
    if summ + p[0] <= M:
        summ += p[0]
        sum_prod.append(p)

print(summ)
print( sum(s[1] == 0 for s in sum_prod))

# if sum_prod[-1][1] == 1:
#     sum_prod = sum_prod[:-1]
#     summ -= sum_prod[-1][0]
#     for p in prod:
#         if p[0] > sum_prod[-1][0]:
#             if p[1] == 0 and summ + p[0] <= M:

len_sum_prod = len(sum_prod)
for price_1 in sum_prod[::-1]:
    if price_1[1]:
        for price_2 in prod[len_sum_prod:]:
            len_sum_prod += 1
            if price_2[1] == 0:
                if summ - price_1[0] + price_2[0] <= M:
                    sum_prod.remove(price_1)
                    sum_prod.append(price_2)
                    summ += -price_1[0] + price_2[0]
                    break

print(sum(s[1] == 0 for s in sum_prod), M - summ)