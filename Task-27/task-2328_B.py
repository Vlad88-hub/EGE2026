from itertools import combinations
from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'./files/27_B_23284.txt') as file:
    N = file.readline()
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

cluster_1 = [dot for dot in dots if 5 < dot[0] < 10]
cluster_2 = [dot for dot in dots if 10 < dot[0] < 20]
cluster_3 = [dot for dot in dots if 20 < dot[0]]

clusters = [cluster_1, cluster_2, cluster_3]

centers = [center(cluster) for cluster in clusters]

min_sum = min(dist(cl1, cl2) for cl1, cl2 in combinations(centers, 2))
max_sum = max(dist(cl1, cl2) for cl1, cl2 in combinations(centers, 2))

print(min_sum*10_000)
print(max_sum*10_000)
