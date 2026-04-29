from ctypes import c_ssize_t
from math import dist

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
            stars.append(list(map(float, [x, y])))

cluster_1 = [dot for dot in dots if dot[1] < 16]
cluster_2 = [dot for dot in dots if 24 > dot[1] > 16]
cluster_3 = [dot for dot in dots if 24 < dot[1]]

stars_in_cluster1 = [s for s in stars if s in cluster_1]
stars_in_cluster2 = [s for s in stars if s in cluster_2]
stars_in_cluster3 = [s for s in stars if s in cluster_3]

res = []
for s in stars_in_cluster1:
    sum_dist = sum(dist(s, s1) for s1 in stars_in_cluster2) + sum(dist(s, s2) for s2 in stars_in_cluster3)
    res.append(sum_dist)

for s in stars_in_cluster2:
    sum_dist = sum(dist(s, s1) for s1 in stars_in_cluster1) + sum(dist(s, s2) for s2 in stars_in_cluster3)
    res.append(sum_dist)

for s in stars_in_cluster3:
    sum_dist = sum(dist(s, s1) for s1 in stars_in_cluster2) + sum(dist(s, s2) for s2 in stars_in_cluster1)
    res.append(sum_dist)

print(max(res)*10_000, min(res)*10_000)
