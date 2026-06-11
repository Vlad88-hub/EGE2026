from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster )
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'./files/27_B_29077.txt') as file:
    dots = []
    stars_7 = []
    stars_4 = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[1] in '89':
            stars_7.append(dots[-1])
        elif data[1] in '123':
            stars_4.append(dots[-1])

cluster_1 = [
    [dot for dot in dots if dot[1] > 21],
    [dot for dot in stars_7 if dot[1] > 21],
    [dot for dot in stars_4 if dot[1] > 21]
]
cluster_2 = [
    [dot for dot in dots if dot[1] < 21 and dot[0] < 20],
    [dot for dot in stars_7 if dot[1] < 21 and dot[0] < 20],
    [dot for dot in stars_4 if dot[1] < 21 and dot[0] < 20]
]
cluster_3 = [
    [dot for dot in dots if dot[1] < 21 and dot[0] > 20],
    [dot for dot in stars_7 if dot[1] < 21 and dot[0] > 20],
    [dot for dot in stars_4 if dot[1] < 21 and dot[0] > 20]
]
clusters = [cluster_1, cluster_2, cluster_3]

max_cluster = max(clusters, key=lambda x: len(x[0]))
min_cluster = min(clusters, key=lambda x: len(x[0]))
med_cluster = [cluster for cluster in clusters if len(cluster[0]) != len(max_cluster[0]) and len(cluster[0]) != len(min_cluster[0])]

print(len(max_cluster[1]), len(med_cluster[0][2]))