with open(r'../files/26_23570.txt') as file:
    N, K = map(int, file.readline().split())
    ter = [int(file.readline()) for i in range(N)]
    mod = [list(map(int, file.readline().split())) for j in range(K)]

ter = sorted(ter)
mod = sorted(mod, key=lambda x: [x[1], -x[0]])

new_mod = {}
for m in mod:
    if m[0] not in new_mod:
        new_mod[m[0]] = [m[1]]
    else:
        new_mod[m[0]] += [m[1]]

price_last_mad = 0
summ = []
for t in ter:
    for m in new_mod:
        if m >= t:
            price_last_mad = [min(new_mod[m]), m]
            summ.append(min(new_mod[m]))
            break

max_mod = 0
for m in sorted(new_mod, reverse=True):
    if min(new_mod[m]) <= price_last_mad[0]:
        max_mod = max(price_last_mad[1], m)
        break

print(sum(summ), max_mod)

####################################################

# ter = sorted(ter)
# mod = sorted(mod, key=lambda x: [x[1], -x[0]])
#
# ans = []
# for t in ter:
#     for m in mod.copy():
#         if m[0] >= t:
#             ans.append([m[1], m[0]])
#             break
#         else:
#             mod.remove(m)
#
#
# print(sum(i[0] for i in ans), ans[-1][1])

