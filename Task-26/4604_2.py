with open(r'.\files\26_4604.txt') as file:
    N = int(file.readline())
    boxes = [int(i) for i in file]

boxes = sorted(boxes, reverse=True)

all_boxes = [boxes[0]]

for box in boxes:
    if all_boxes[-1] - box >= 3:
        all_boxes.append(box)

print(len(all_boxes), all_boxes[-1])