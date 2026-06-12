with open(r'../files/26_21910.txt') as file:
    N = file.readline()
    boxes = [int(i) for i in file]

boxes = sorted(boxes, reverse=True)

last_box = [boxes[0]]
for box in boxes[1:]:
    if last_box[-1] - box >= 9:
        last_box.append(box)

print(len(last_box), last_box[-1])