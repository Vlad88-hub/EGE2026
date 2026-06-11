with open(r'../files/26_12256.txt') as file:
    S, N  = map(int, file.readline().split())
    items = [int(i) for i in file]

items = sorted(items)

sad = []
for it in items:
    if sum(sad) + it <= S:
        sad.append(it)

sad = sad[:-1]
max_it = 0
for it in items:
    if it > sad[-1]:
        if sum(sad) + it <= S:
            max_it = max(max_it, it)

print(len(sad)+1, max_it)
