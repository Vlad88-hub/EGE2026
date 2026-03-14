with open(r'.\files\26_4712.txt') as file:
    N = int(file.readline())
    boxes = [int(i) for i in file]

boxes = sorted(boxes, reverse=True)
last_box = boxes[0]
cnt = 1
for i in boxes:
    if last_box - i >= 3:
        last_box = i
        cnt += 1

print(cnt, last_box)