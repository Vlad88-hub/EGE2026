with open(r'../files/26_3230.txt') as file:
    N = file.readline()
    sad = [list(map(int, i.split())) for i in file]

sad = sorted(sad, key=lambda x: (-x[0], x[1]))

for s1, s2 in zip(sad, sad[1:]):
    if s1[0] == s2[0]:
        if s2[1] - s1[1] == 12:
            print(s1[0], s1[1]+1)
            break