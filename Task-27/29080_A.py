from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'./files/27_A_29080.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',','.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'L' and data[1] == '3':
            stars.append(dots[-1])

cluster_1 = [
    [dot for dot in dots if dot[1] < 8],
    [dot for dot in stars if dot[1] < 8],
]
cluster_2 = [
    [dot for dot in dots if dot[1] > 8],
    [dot for dot in stars if dot[1] > 8]
]
clusters = [cluster_1, cluster_2]

min_cluster = min(clusters, key= lambda x: len(x[0]))
max_cluster = max(clusters, key= lambda x: len(x[0]))

max_dist_1 = max(dist(center(min_cluster[0]), s) for s in stars)
max_dist_2 = max(dist(center(max_cluster[0]), s) for s in stars)

print(max_dist_1*10_000, max_dist_2*10_000)