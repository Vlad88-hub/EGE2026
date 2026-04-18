with open(r'./files/26_21424.txt') as file:
    N = int(file.readline())
    boxes = [int(i) for i in file]

boxes = sorted(boxes, reverse=True)
last_boxes = [boxes[0]]

for box in boxes[1:]:
    if last_boxes[-1] - box >= 9:
        last_boxes += [box]

print(len(last_boxes), last_boxes[-1])