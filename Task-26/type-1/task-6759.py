with open(r'../files/26_6759.txt') as file:
    N = int(file.readline())
    prices = [int(i) for i in file]

prices = sorted(prices)
k = N //3

sum_1 = sum(prices) - sum(prices[-k:])
sum_2 = sum(prices) - sum(i for i in prices[::-1][2::3])

print(sum_1, sum_2)

data = '1234'
print(data[:2])
