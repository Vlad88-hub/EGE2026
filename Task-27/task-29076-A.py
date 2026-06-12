from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist= sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]


with open(r'./files/27_A_29076.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[1] == '2':
            stars.append(dots[-1])

cluster_1 = [
    [dot for dot in dots if dot[1] < 8],
    [dot for dot in stars if dot[1] < 8]
]
cluster_2 = [
    [dot for dot in dots if dot[1] > 8],
    [dot for dot in stars if dot[1] > 8],
]
clusters = [cluster_1, cluster_2]

min_clus = min(clusters, key=lambda x: len(x[1]))
max_clus = max(clusters, key=lambda x: len(x[1]))

print(center(min_clus[0])[0] * 10_000, center(max_clus[0])[1] * 10_000)