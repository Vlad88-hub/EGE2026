with open(r'./files/26_18541.txt') as file:
    N, M = map(int, file.readline().split())
    data = [int(i) for i in file]

weights_sports = data[N:]
av_weights = data[:N]

weights_sports = sorted(weights_sports, reverse=True)
av_weights = sorted(av_weights, reverse=True)

weights_completed = []
for i in weights_sports:
    for n in av_weights:
        if i - n >= 0:
            weights_completed.append(n)
            break

often_weight = max([weights_completed.count(n), n] for n in set(weights_completed))[1]

print(sum(weights_completed)/len(weights_completed))
print(often_weight)







# s = '123224423'
# print(s[-4:])
# print(s[:-4])
