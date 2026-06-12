with open(r'../files/26_23283.txt') as file:
    K = int(file.readline())
    N = int(file.readline())
    person = [list(map(int, i.split())) for i in file]

person = sorted(person)

ok = [0] * (K+1)
last_person = cnt = 0
for per in person:
    for i in range(1, K+1):
        if ok[i] < per[0]:
            ok[i] = per[1]
            cnt += 1
            last_person = i
            break

print(cnt, last_person)


