from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'./files/27A_27138.txt') as file:
    dots = [list(map(float, i.replace(',','.').split())) for i in file]

eps = 0.8
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

print((centers[0][0] - centers[1][0]) * 10_000)
print((centers[0][1] - centers[1][1]) * 10_000)

with open(r'./files/27B_27138.txt') as file:
    dots = [list(map(float, i.replace(',','.').split())) for i in file]


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

len_cluster = sorted([len(cluster), cluster] for cluster in clusters)
len_cluster1 = len_cluster[1][1]
max_abs = max(dot[0] for dot in len_cluster1)

res_1 = []
for dot in clusters[0]:
    sum_dist = sum(dist(dot, d) for d in clusters[1]) + sum(dist(dot, d) for d in clusters[2])
    res_1.append([sum_dist, dot])
res_1_max = max(res_1)

res_2 = []
for dot in clusters[1]:
    sum_dist = sum(dist(dot, d) for d in clusters[0]) + sum(dist(dot, d) for d in clusters[2])
    res_2.append([sum_dist, dot])
res_2_max = max(res_2)

res_3 = []
for dot in clusters[2]:
    sum_dist = sum(dist(dot, d) for d in clusters[0]) + sum(dist(dot, d) for d in clusters[1])
    res_3.append([sum_dist, dot])
res_3_max = max(res_3)

max_res = max(res_1_max,res_2_max,res_3_max)[1]

print(max_abs * 10_000)
print((max_res[0] + max_res[1])*10_000)