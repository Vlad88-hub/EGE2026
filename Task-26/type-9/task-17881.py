with open(r'../files/26_17881.txt') as file:
    N = int(file.readline())
    stud = []
    for i in file:
        idd, x, y, z, w = map(int, i.split())
        bl = [x, y, z, w]
        cnt_2 = [i == 2 for i in bl]
        stud.append([idd,sum(bl)/4, sum(cnt_2)])

stud = sorted(stud, key=lambda x: (x[-1], -x[1], x[0]))
k = N//4
# print(stud, k)

print(stud[:k][-1][0])
last_stud = 0
for i in stud:
    if i[-1] > 2:
        print(i[0])
        break




# data = '1234'
# print(data[:2])

