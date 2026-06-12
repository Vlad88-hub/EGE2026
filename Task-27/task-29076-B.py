from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'./files/27_B_29076 (1).txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',','.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'Y':
            stars.append(list(map(float, [x, y])))

cluster_1 = [
    [dot for dot in dots if dot[1] < 16],
    [dot for dot in stars if dot[1] < 16],
]
cluster_2 = [
    [dot for dot in dots if 22 > dot[1] > 16],
    [dot for dot in stars if 22 > dot[1] > 16],
]
cluster_3 = [
    [dot for dot in dots if 22 < dot[1]],
    [dot for dot in stars if 22 < dot[1]],
]
clusters = [cluster_1, cluster_2, cluster_3]

min_clus = min(clusters, key=lambda x: len(x[1]))
max_clus = max(clusters, key=lambda x: len(x[1]))
dist_1 = dist(center(min_clus[0]), center(max_clus[0]))

max_dist = max(dist(center(cl[0]), j) for cl in clusters for j in cl[1])

# max_1 = max([dist(center(cluster_1[0]), s) for s in cluster_1[1]] + [dist(center(cluster_2[0]), s) for s in cluster_2[1]] + [dist(center(cluster_3[0]), s) for s in cluster_3[1]])

print(dist_1*10_000, max_dist*10_000)