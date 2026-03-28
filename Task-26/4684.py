with open(r'.\files\26_4684.txt') as file:
    N = int(file.readline())
    data = [int(i) for i in file]

data = sorted(data,reverse=True)
cnt_t = N // 6

sum_many = sum([n for n in data]) - sum([n for n in data[5::6]]) // 2

sum_one = sum(data) - sum(data[-cnt_t:])//2

print(sum_many, sum_one)