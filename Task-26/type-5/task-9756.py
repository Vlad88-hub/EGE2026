with open(r'../files/26_9756.txt') as file:
    N = file.readline()
    events = [list(map(int, i.split())) for i in file]

events = sorted(events, key=lambda x: (x[1], x[0]))

# cnt = 1
# last_event = events[0][1]
# for event in events:
#     if last_event <= event[0]:
#         cnt += 1
#         last_event = event[1]
#     elif last_event == event[0]:
#         cnt += 1
#         last_event = max(event[1], last_event)
#
# print(cnt, last_event)

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