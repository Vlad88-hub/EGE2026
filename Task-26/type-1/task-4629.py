with open(r'../files/26_4629.txt') as file:
    N = int(file.readline())
    prices = [int(i) for i in file]

prices = sorted(prices)
k = N // 4
# print(prices)
sum_1 = sum(prices[:-k]) + sum(prices[-k:])/2
sum_2 = sum(prices[k:]) + sum(prices[:k])/ 2

print(sum_1, sum_2)

# data = '1234'
# print(prices[-k:])