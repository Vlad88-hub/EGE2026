with open(r'./files/26_27636.txt') as file:
    N = list(map(int, file.readline().split()))
    boxes = [int(i) for i in file]

boxes = sorted(boxes, reverse=True)
S = N[0]

sum_mass = []

# for box in boxes.copy():
#     if sum(sum_mass) < S:
#         sum_mass += [box]
while sum(sum_mass) <= S:
    sum_mass += [boxes.pop()]

print(len(sum_mass), len(boxes), sum(boxes))