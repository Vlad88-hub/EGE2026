with open(r'../files/26_19256.txt') as file:
    N = int(file.readline())
    stud = {}
    for i in file:
        idd, num = map(int, i.split())
        if idd not in stud:
            stud[idd] = [num]
        elif num in stud[idd]:
            continue
        else:
            stud[idd] += [num]


comp =[]
for idd in stud:
    stud[idd] = sorted(stud[idd])
    cnt_num = 1
    for i in range(len(stud[idd]) - 1):
        if stud[idd][i + 1] - stud[idd][i] == 1:
            cnt_num += 1
        else:
            comp.append([cnt_num, idd])
            cnt_num = 1
    comp.append([cnt_num, idd])


print(max(comp, key=lambda x: (x[0], -x[1])))