with open(r'../files/26_17687.txt') as file:
    N = int(file.readline())
    prices = [int(i) for i in file]

prices = sorted(prices)
k = N // 9

sum_1 = sum(prices) - sum(prices[-k:])
sum_2 = sum(prices) - sum(prices[::-1][8::9])

print(sum_1, sum_2)