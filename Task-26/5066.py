# def f(boxes):
#     all_box = [boxes[0]]
#     for box in boxes:
#         if all_box[-1] - box >= 7:
#             all_box += [box]
#     return all_box

with open(r'.\files\26_5066.txt') as file:
    N = int(file.readline())
    boxes = [int(i) for i in file]


boxes = sorted(boxes, reverse=True)

# new_boxes = boxes
# max_boxes = f(boxes)
#
# ans = 0
# while new_boxes:
#     m_boxes = f(new_boxes)
#     for i in m_boxes:
#         new_boxes.remove(i)
#     ans += 1
#
# print(ans, len(max_boxes))

# blocks = []
# while boxes:
#     block = [boxes[0]]
#     boxes.remove(boxes[0])
#     for box in boxes[:]:
#         if block[-1] - box >= 7:
#             block += [box]
#             boxes.remove(box)
#     blocks += [len(block)]
#
# print(len(blocks), max(blocks))

with open(r'..\..\..\Files\26_5066.txt') as file:
    N = file.readline()
    containers = sorted(int(i) for i in file)[::-1]

amount_of_blocks = 0

while containers:
    previous_container = containers[0]
    containers.remove(containers[0])
    for container in containers:
        if container > 0 and previous_container - container >= 7:
            previous_container = container
            containers[containers.index(previous_container)] = -1
    while -1 in containers:
        containers.remove(-1)
    amount_of_blocks += 1

print(amount_of_blocks)