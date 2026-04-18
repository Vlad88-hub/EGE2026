from math import floor, ceil

with open(r'.\files\26_20161.txt') as file:
    N = int(file.readline())
    goods = [list(map(int, i.split())) for i in file]

chet_goods = sorted([i for i in goods if i[1] % 2 == 0])
ne_chet_goods = sorted([i for i in goods if i[1] % 2 != 0])

new_chet_goods = [i[0] for i in chet_goods]
cnt_count_chet = floor(len(new_chet_goods) * 7 / 10)
sum_chet_goods = sum([floor(i * 7 / 10) for i in new_chet_goods[:cnt_count_chet]]) \
                 + sum([floor(i * 8 / 10) for i in new_chet_goods[cnt_count_chet:]])

new_ne_chet_goods = [i[0] for i in ne_chet_goods]
cnt_count_ne_chet = floor(len(ne_chet_goods) * 25 / 100)
sum_ne_chet_goods = sum(new_ne_chet_goods) - sum([ceil(i * 15 / 100) for i in new_ne_chet_goods[-cnt_count_ne_chet:]])

sum_chet_discount = sum(new_chet_goods) - sum_chet_goods
sum_ne_chet_discount = sum(new_ne_chet_goods) - sum_ne_chet_goods

print(sum_chet_goods + sum_ne_chet_goods)
print(sum_chet_discount - sum_ne_chet_discount)
# data = '1132412345568'
# print(data[:8])
# print(data[8:])