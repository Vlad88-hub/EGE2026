with open(r'../files/26_2_23175.txt') as file:
    N, M = map(int, file.readline().split())
    boxes = []
    weight = []
    for i in file:
        if len(weight) != N:
            weight.append(int(i))
        else:
            boxes.append(int(i))

weight = sorted(weight)
boxes = sorted(boxes)

weight_copy = weight
boxes_2 = []
for box in boxes:
    for w in weight_copy:
        if box >= w:
            boxes_2.append([w, box])
            weight_copy.remove(w)
            break

last_box = boxes_2[-1][1]
last_weight = 0
for w in weight[::-1]:
    if last_box >= w:
        last_weight = w
        break


print(len(boxes_2), last_weight - boxes_2[-2][0])

