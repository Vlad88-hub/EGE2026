with open(r'.\files\26_4660.txt') as file:
    N = int(file.readline())
    data = [int(i) for i in file]

# data = [11,30,40,20,40,56,78,90,88]

data = sorted(data, reverse=True)

# sum_client = 0
# cnt = 0
# for n in data:
#     cnt += 1
#     if cnt == 4:
#         sum_client += n // 2
#         cnt = 0
#     else:
#         sum_client += n


summ = sum([n for n in data]) - sum([n for n in data[3::4]])//2

cnt_t = N // 4

sum_store = sum(data) - sum(data[-cnt_t:]) // 2
print(summ, sum_store)
# print(sum_client, sum_store)