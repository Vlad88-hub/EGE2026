with open(r'../files/26_4205.txt') as file:
    N = file.readline()
    sad = [list(map(int, i.split())) for i in file]

sad = sorted(sad, key=lambda x: (-x[0], x[1]))
# print(sad)

for s1, s2 in zip(sad, sad[1:]):
    # cnt = []
    if s1[0] == s2[0]:
        if s2[1] - s1[1] == 14:
            print(s1[0], s1[1]+1)
            break
            # cnt.append(s1[1] + 1)
            # if len(cnt) == 13:
            #     print(s1[0], min(cnt))
    else:
        cnt = []