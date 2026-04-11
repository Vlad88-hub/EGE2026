from math import floor
with open(r'.\files\26.6_13394.txt') as file:
    N = int(file.readline())
    data = [int(i) for i in file]

data = sorted(data, reverse=True)

new_min_data = [i for i in data if i <= 350]
new_max_data = [i for i in data if i > 350]
cnt = len(new_max_data) // 3

sum_pay_shop = sum(new_min_data) + (sum(new_max_data) - sum(floor(i * 0.75)for i in new_max_data[2::3]))

sum_pay_one_bill = sum(new_min_data) + sum(new_max_data[:-cnt]) + sum(new_max_data[-cnt:])/4

print(sum_pay_shop, sum_pay_one_bill)

###########################################################################3

k = 3
sum_pay_many_bill = sum(data) -  sum(new_max_data[k - 1:: k])/4
sum1_pay_many_bill = sum(data) -  sum(floor(i * 0.75) for i in new_max_data[k - 1:: k])
sum_pay_one_bill = sum(data) - sum(new_max_data[- len(new_max_data) // k:])* 0.75

print(sum1_pay_many_bill, sum_pay_one_bill)
# fil = '1234988'
# print(fil[-2:])
