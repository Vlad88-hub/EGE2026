with open(r'.\files\26_12113.txt') as file:
    N = int(file.readline())
    boxes = [int(i) for i in file]

boxes = sorted(boxes, reverse=True)

last_box = max(boxes)
u = last_box % 2 == 0
cnt = 1
for box in boxes:
    if last_box - box >= 7 and (box % 2 == 0) != u:
        cnt += 1
        last_box = box
        u = box % 2 == 0

print(cnt, last_box)