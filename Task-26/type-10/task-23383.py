with open(r'../files/26_23383.txt') as file:
    N = int(file.readline())
    chek = {}
    for i in file:
        sport, idd = map(int, i.split())
        if idd not in chek:
            chek[idd] = [sport]
        elif sport in chek[idd]:
            continue
        else:
            chek[idd] += [sport]

comp = []
for idd in chek:
    chek[idd] = sorted(chek[idd])
    cnt_sport = 1
    for i in range(len(chek[idd]) - 1):
        if chek[idd][i+1] - chek[idd][i] == 1:
            cnt_sport += 1
        else:
            comp.append([cnt_sport, idd])
            cnt_sport = 1
    comp.append([cnt_sport, idd])

print(max(comp, key=lambda x: (x[0], -x[1])))