with open(r'.\files\26_17687.txt') as file:
    N = int(file.readline())
    data = [int(i) for i in file]

data = sorted(data, reverse=True)
cnt = N // 9

sum_pay_shop = sum(data) - sum(data[8::9])

sum_pay_client = sum(data) - sum(data[:cnt])

print(sum_pay_client, sum_pay_shop)