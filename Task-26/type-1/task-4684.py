with open(r'../files/26_4684.txt') as file:
    N = int(file.readline())
    prices = [int(i) for i in file]

prices = sorted(prices, reverse=True)
k = N // 6

sum_1 = sum(prices) - sum(i for i in prices[5::6])/2
sum_2 = sum(prices[-k:])/2 + sum(prices[:-k])

print(sum_1, sum_2)