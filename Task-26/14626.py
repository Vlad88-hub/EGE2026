with open(r'./files/26_14626.txt') as file:
    N = int(file.readline())
    K,M = map(int, file.readline().split())
    caves = {}
    for id in sorted(map(int, file.readline().split())):
        caves[id] = M
    weights = sorted(int(i) for i in file)

ans = []
abs2 = []
for id in caves:
    cave = caves[id]
    len_weights = len(weights)
    for maximum, minimum in list(zip(weights[::-1], weights))[:len(weights)//2]:
        # if weights.index(maximum) - weights.index(minimum)
        if minimum <= cave:
            cave -= maximum
            weights.remove(maximum)
        else:
            break
        if minimum <= cave:
            cave -= minimum
            weights.remove(minimum)
    else:
        if len_weights % 2 != 0:
            len_weights = len(weights)
            if weights[len_weights // 2] <= cave:
                cave -= weights[len_weights // 2]
                weights.remove(weights[len_weights // 2])
    ans.append([cave, id])
    if cave != M:
        abs2 += cave

print(min(ans, key=lambda x: (x[0], -x[1]))[1])
print(abs2)