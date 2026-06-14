from math import dist
from itertools import combinations

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'./files/27_B_29074.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'L' and data[2:] == 'V':
            stars.append(dots[-1])

cluster_1 = [
    [dot for dot in dots if dot[1] > 22],
    [dot for dot in stars if dot[1] > 22]
]
cluster_2 = [
    [dot for dot in dots if dot[1] < 22 and dot[0] < 20],
    [dot for dot in stars if dot[1] < 22 and dot[0] < 20]
]
cluster_3 = [
    [dot for dot in dots if dot[1] < 22 and dot[0] > 20],
    [dot for dot in stars if dot[1] < 22 and dot[0] > 20]
]
clusters = [cluster_1, cluster_2, cluster_3]

min_dist = min(dist(center(cl[0]), s1) for cl in clusters for s1 in cl[1])
max_dist = max(dist(center(cl[0]), s1) for cl in clusters for s1 in cl[1])

print(min_dist*10_000, max_dist*10_000)