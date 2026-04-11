with open(r'./files/26_589.txt') as file:
    N = int(file.readline())
    price = [int(i) for i in file]

price = sorted(price)

price_next = price[0]

cnt = 1
summ = []
summ_2 = []
for prices in price:
    if price_next - prices in range(0, 500):
        cnt += 1
        if cnt % 2 == 0:
            summ += [prices / 2]
            summ_2 += [prices / 2]
            price_next = prices
        else:
            price_next = prices
            summ += [prices]
    else:
        price_next = prices
        cnt = 1
        summ += [prices]

print(sum(price) - sum(summ), max(summ_2))

####################################################################

# for i in range(0, max(price) // 500 + 1):
#     group = [j for j in price if i * 500 < j <= (i + 1) * 500]

sum_sail = 0
sail = 0
for i in range(0, max(price), 500):
    group = [j for j in price if i < j <= i + 500]
    sail += sum(group[:len(group) // 2]) / 2
    sum_sail = max(sum_sail, max(group[:len(group) // 2])) // 2

print(sum_sail, sail)
