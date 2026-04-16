from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'./files/27_A_23209.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

cluster_A_1 = [dot for dot in dots if dot[0] < 5]
cluster_A_2 = [dot for dot in dots if dot[0] > 5]

center_A_1 = center(cluster_A_1)
center_A_2 = center(cluster_A_2)

print(max(center_A_1[0], center_A_2[0]) * 10_000, max(center_A_1[1], center_A_2[1]) * 10_000)

with open(r'./files/27_B_23209.txt') as file:
    dots_2 = [list(map(float, i.replace(',', '.').split())) for i in file]

cluster_B_1 = [dot for dot in dots_2 if 30 > dot[1] > 21]
cluster_B_2 = [dot for dot in dots_2 if 10 < dot[1] < 21 ]
cluster_B_3 = [dot for dot in dots_2 if 0 < dot[1] < 10 ]

center_B_1 = center(cluster_B_1)
center_B_2 = center(cluster_B_2)
center_B_3 = center(cluster_B_3)

list_clusters = [cluster_B_1, cluster_B_2, cluster_B_3]

max_lens_cluster = max(len(i) for i in list_clusters)
min_lens_cluster = min(len(i) for i in list_clusters)

max_center_B_1_2 = [center(f) for f in list_clusters if len(f) == max_lens_cluster]
min_center_B_1_2 = [center(f) for f in list_clusters if len(f) == min_lens_cluster]

print((max_center_B_1_2[0][0] - min_center_B_1_2[0][0])*10_000)
print((max_center_B_1_2[0][1] - min_center_B_1_2[0][1])*10_000)