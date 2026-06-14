with open(r'../files/26_9756 (1).txt') as file:
    N = file.readline()
    events = [list(map(int, i.split())) for i in file]

events = sorted(events, key=lambda x: (x[1], x[0]))

approved = [events[0]]
for event in events:
    if approved[-1][1] <= event[0]:
        approved.append(event)

approved = approved[:-1]
for event in events[::-1]:
    if approved[-1][1] <= event[0]:
        approved.append(event)
        break

print(len(approved), approved[-1][1])