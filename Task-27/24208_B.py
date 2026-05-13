from math import  dist
from itertools import combinations

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'./files/27B_24208.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

eps = 1.2
clusters = []

while dots:
    cluster = [dots.pop()]
    for dot in cluster:
        for d in dots.copy():
            if dist(dot, d) < eps:
                cluster.append(d)
                dots.remove(d)
    if len(cluster) > 1:
        clusters.append(cluster)

centers = [center(cluster) for cluster in clusters]

dist_centers = [dist(x, y) for x, y in combinations(centers, 2)]

print(min(dist_centers)*10_000)
print(max(dist_centers)*10_000)
# test = [[1],[2],[3]]
#
# print(*combinations(test, 2))