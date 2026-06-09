with open(r'../files/26_4604.txt') as file:
    N = file.readline()
    boxes = [int(i) for i in file]

boxes = sorted(boxes, reverse=True)

new_boxes = [boxes[0]]
for box in boxes[1:]:
    if new_boxes[-1] - box >= 3:
        new_boxes.append(box)


print(len(new_boxes), new_boxes[-1])