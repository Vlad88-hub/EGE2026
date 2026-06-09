from math import dist
from itertools import combinations

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'./files/27_B_29080.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'L':
            stars.append(dots[-1])

custer_1 = [
    [dot for dot in dots if dot[1] > 22],
    [dot for dot in stars if dot[1] > 22]
]
cluster_2 = [
    [dot for dot in dots if 22 > dot[1] > 16],
    [dot for dot in stars if 22 > dot[1] > 16]
]
cluster_3 = [
    [dot for dot in dots if dot[1] < 16],
    [dot for dot in stars if dot[1] < 16]
]
clusters = [custer_1,cluster_2,cluster_3]

max_stars = max(clusters, key=lambda x: len(x[1]))
min_stars = min(clusters, key=lambda x: len(x[1]))
dist_1 = dist(center(max_stars[0]), center(min_stars[0]))

max_dist_stars = max(dist(s1, s2) for cl1, cl2 in combinations(clusters, 2) for s1 in cl1[1] for s2 in cl2[1])

print(dist_1*10_000, max_dist_stars*10_000)