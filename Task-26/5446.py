with open(r'.\files\26_5446.txt') as file:
    N = int(file.readline())
    tubes = [tuple(map(int, i.split())) for i in file]

tubes = sorted(tubes, key=lambda x: (-x[0] + 2 * x[1]))

all_tubes = [tubes[0]]

for tube in tubes:
    if all_tubes[-1][0] - 2 * all_tubes[-1][1] - tube[0] >= 3:
        all_tubes += [tube]

all_tubes = all_tubes[:-1]

for tube in sorted(tubes, key=lambda x: -x[0]):
    if all_tubes[-1][0] - 2 * all_tubes[-1][1] - tube[0] >= 3:
        all_tubes += [tube]
        break

print(len(all_tubes), all_tubes[-1][0])

##############################################3

# with open('26_5446.txt') as file:
#     n = int(file.readline())
#     pipes = []
#     for i in file:
#         pipes.append(list(map(int, i.split())))
# pipes = sorted(pipes, key=lambda x: (-x[0] + x[1]))
# big = pipes[0]
# ans = [big[0]]
# for pipe in pipes:
#     if big[0] - big[1] * 2 - pipe[0] >= 3:
#         ans.append(pipe[0])
#         big = pipe
# print(len(ans), ans[-1])