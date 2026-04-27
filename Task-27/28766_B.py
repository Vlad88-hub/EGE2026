from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'./files/27_B_28766.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',','.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'Z' and data[2:] == 'I':
            stars.append(list(map(float, [x, y])))

eps = 1
clusters = []

while dots:
    cluster = [dots.pop()]
    for dot in cluster:
        for d in dots.copy():
            if dist(dot, d) < eps:
                cluster.append(d)
                dots.remove(d)
    clusters.append(cluster)

stars_clusters_1 = [s for s in stars for dot in clusters[0] if s == dot]
stars_clusters_2 = [s for s in stars for dot in clusters[1] if s == dot]
stars_clusters_3 = [s for s in stars for dot in clusters[2] if s == dot]

min_dist_1 = min([dist(s1, s2) for s1 in stars_clusters_1 for s2 in stars_clusters_1 if s1 != s2])
min_dist_2 = min([dist(s1, s2) for s1 in stars_clusters_2 for s2 in stars_clusters_2 if s1 != s2])
min_dist = [min_dist_1*10_000, min_dist_2*10_000]

print(min(min_dist))

center_1 = center(clusters[0])
center_2 = center(clusters[2])

print(dist(center_2, center_1)*10_000)

################################################

from itertools import combinations
from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'.\files\27_B_28766.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'Z' and data[2:] == 'I':
            stars.append(list(map(float, [x, y])))

cluster_1 = [
    [d for d in dots if 23 < d[1]],
    [d for d in stars if 23 < d[1]]
]

cluster_2 = [
    [d for d in dots if 16 < d[1] < 23],
    [d for d in stars if 16 < d[1] < 23]
]

cluster_3 = [
    [d for d in dots if d[1] < 16],
    [d for d in stars if d[1] < 16]
]

clusters = [cluster_1, cluster_2, cluster_3]

dists = []
for cluster in clusters:
    dists += [dist(d1, d2) for d1, d2 in combinations(cluster[1], 2)]
B1 = min(dists)

max_cluster = center(max(clusters, key=lambda x: len(x[1]))[0])
min_cluster = center(min(clusters, key=lambda x: len(x[1]))[0])
B2 = dist(max_cluster, min_cluster)

print(B1 * 10_000, B2 * 10_000)
