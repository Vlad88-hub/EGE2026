from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster )
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'./files/27_A_29077.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'N' and data[1] == '9' and data[2:] == 'I':
            stars.append(dots[-1])

cluster_1 = [
    [dot for dot in dots if dot[1] < 8]
    # [dot for dot in stars if dot[1] < 8]
]
cluster_2 = [
    [dot for dot in dots if dot[1] > 8]
    # [dot for dot in stars if dot[1] > 8]
]
clusters = [cluster_1, cluster_2]

dist_center_min = min(dist(center(cluster[0]), stars[0]) for cluster in clusters)
dist_center_max = max(dist(center(cluster[0]), stars[0]) for cluster in clusters)


print(dist_center_min*10_000, dist_center_max*10_000)