with open(r'.\files\26_17786.txt') as file:
    N, V = file.readline().split()
    data = [int(i) for i in file]

data = sorted(data, reverse=True)

data_max = max([i for i in data if 7000 <= i <= 12000 ])
data.remove(data_max)
V = int(V) - data_max / 1000

ans = []
cnt = 1
for n in data:
    if  7000 <= n <= 12000 and V - n / 1000 >= 0:
        ans += [n]
        cnt += 1
        V -= n / 1000
print(cnt, min(ans))



