with open(r'../files/26_3586.txt') as file:
    N = file.readline()
    sad = [list(map(int, i.split())) for i in file]

sad = sorted(sad, key=lambda x: (-x[0], x[1]))

max_prop = []
for s1, s2 in zip(sad, sad[1:]):
    if s1[0] == s2[0]:
        max_prop.append([s2[1] - s1[1] - 1, s1[0]])

print(max(max_prop))
