with open(r'.\files\26_4629.txt') as file:
    N = file.readline()
    data = [int(i) for i in file]

data = sorted(data)
cnt_t = int(N) // 4

# summ_client = sum(data) - sum(data[-cnt_t:]) // 2
# store = sum(data) - sum(data[:cnt_t]) // 2

sum_client = sum([n for n in data[:-cnt_t]]) + sum([n for n in data[-cnt_t:]])//2
sum_store = sum([n for n in data[cnt_t:]]) + sum([n for n in data[:cnt_t]])//2

print(sum_client, sum_store)

data1 = '122342312'
print(data1[3::4])

