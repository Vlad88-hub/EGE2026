with open(r'../files/26_23208.txt') as file:
    N = int(file.readline())
    det = []
    cnt = 0
    for i in file:
        cnt += 1
        x, y = map(int, i.split())
        if x < y:
            det.append([x, 0, cnt])
        else:
            det.append([y, 1, cnt])

det = sorted(det, key=lambda x: (x[1],x[0]))
print(max(det), sum(i[1] == 0 for i in det))

