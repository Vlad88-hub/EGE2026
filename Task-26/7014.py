with open(r'./files/26_7014.txt') as file:
    N = int(file.readline())
    data = [int(i) for i in file]

max_earning_per_day = 0
sum_earning = 0

while data:
    data_max = max(data)
    pos = len(data) - data[::-1].index(max(data)) - 1
    earning_per_day = (pos + 1) * data_max
    sum_earning += earning_per_day
    max_earning_per_day = max(max_earning_per_day, earning_per_day)
    data = data[pos + 1:]

print(sum_earning, max_earning_per_day)