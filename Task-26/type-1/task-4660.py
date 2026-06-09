with open(r'../files/26_4660.txt') as file:
    N = int(file.readline())
    prices = [int(i) for i in file]

prices = sorted(prices, reverse=True)
k = N // 4

sum_1 = sum(prices) - sum(i / 2 for i in prices[3::4])
sum_2 = sum(prices[-k:])/2 + sum(prices[:-k])

print(sum_1, sum_2)
# data = '1234'
# print(data[:2])