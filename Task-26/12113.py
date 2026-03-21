with open(r'.\files\26_12113.txt') as file:
    N = int(file.readline())
    boxes = [int(i) for i in file]

boxes = sorted(boxes, reverse=True)

red = [max(i for i in boxes if i % 2 == 1)]
blue = [max(i for i in boxes if i % 2 == 0)]

for box in boxes:
    if red[-1] % 2 != box % 2 and red[-1] - box >= 7:
        red.append(box)
    if blue[-1] % 2 != box % 2 and blue[-1] - box >= 7:
        blue.append(box)

print(len(red), red[-1])
print(len(blue), blue[-1])