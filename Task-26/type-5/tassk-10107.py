with open(r'../files/26_10107.txt') as file:
    N = file.readline()
    times = [list(map(int, i.split())) for i in file]

# times = [[10, 150], [100, 120], [131,170], [150, 180], [120, 130]]
times = sorted(times, key=lambda x: (x[1], x[0]))


last_person = [times[0]]
for person in times:
    # print(person)
    if last_person[-1][1] <= person[0]:
        last_person.append(person)


last_person = last_person[:-1]
last_person.append(max(times))

print(len(last_person), last_person[-1][0] - last_person[-2][1])

