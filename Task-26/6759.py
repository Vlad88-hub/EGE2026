with open(r'.\files\26_6759.txt') as file:
    N = int(file.readline())
    data = [int(i) for i in file]

data = sorted(data, reverse=True)
cnt_t = N // 3
# sum_client = 0
# for i in range(0, len(data), 3):
#     sum_client += sum(data[i:i + 3]) - max(data[i:i + 3])

sum_many = sum([n for n in data]) - sum([n for n in data[2::3]])
sum_store = sum(data) - sum(data[::-1][-cnt_t:])

# sum_store = 0
# for i in range(0, len(data), 3):
#     sum_store += sum(data[i:i + 3]) - min(data[i:i + 3])

print(sum_many, sum_store)