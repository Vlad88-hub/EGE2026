with open(r'../files/26_23208.txt') as file:
    N = file.readline()
    parts = []
    cnt = 0
    for i in file:
        cnt += 1
        x,y = map(int, i.split())
        if x < y:
            parts.append([x, 0, cnt])
        else:
            parts.append([y, 1, cnt])

last_part = max(parts)
print(last_part)
print(sum(x[1] == 0 for x in parts))