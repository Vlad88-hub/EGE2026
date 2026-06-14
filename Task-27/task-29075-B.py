from math import dist
from itertools import combinations

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'./files/27_B_29075.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',','.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'J':
            stars.append(dots[-1])

cluster_1 = [dot for dot in stars if dot[1] < 16]
cluster_2 = [dot for dot in stars if 24 > dot[1] > 16]
cluster_3 = [dot for dot in stars if 24 < dot[1]]

clusters = [cluster_1, cluster_2, cluster_3]

min_dist = min(dist(s1, s2) for cl1, cl2 in combinations(clusters, 2) for s1 in cl1 for s2 in cl2)
max_dist = max(dist(s1, s2) for cl1, cl2 in combinations(clusters, 2) for s1 in cl1 for s2 in cl2)

print(min_dist * 10_000, max_dist * 10_000)
# print(cluster_3)