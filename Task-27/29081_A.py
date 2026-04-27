from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'./files/27_A_29081.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',','.').split()
        dots.append(list(map(float, [x, y])))
        if data[2:] == 'VII':
            stars.append(dots[-1])


cluster_1 = [d for d in dots if d[1] > 8]
cluster_2 = [d for d in dots if d[1] < 8]

stars_1 = [s for s in stars if s[1] > 8]
stars_2 = [s for s in stars if s[1] < 8]

center_1 = center(cluster_1)
center_2 = center(cluster_2)

min_dist_1 = min(dist(center_1, s) for s in stars_1)
min_dist_2 = min(dist(center_2, s) for s in stars_2)
min_dist = min(min_dist_1, min_dist_2)

max_dist_1 = max(dist(center_1, s) for s in stars_1)
max_dist_2 = max(dist(center_2, s) for s in stars_2)
max_dist = max(max_dist_1, max_dist_2)

min_dist_10 = min(min(dist(center_1, s) for s in stars_1), min(dist(center_2, s) for s in stars_2))

print(min_dist * 10_000, max_dist * 10_000, min_dist_10 * 10_000)

########################################################

cluster_1 = [
[d for d in dots if d[1] > 8],
[s for s in stars if s[1] > 8]
]

cluster_2 = [
[d for d in dots if d[1] < 8],
[s for s in stars if s[1] < 8]
]
clusters = [cluster_1, cluster_2]
a = [dist(center(cl[0]), s) for cl in clusters for s in cl[1]]

print(min(a)*10_000, max(a) * 10_000)