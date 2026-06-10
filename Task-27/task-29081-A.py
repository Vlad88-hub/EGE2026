from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[-1]

with open(r'./files/27_A_29081.txt') as file:
    dots = []
    stars = []
    for i in file:
        x,y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[2:] == 'VII':
            stars.append(dots[-1])

cluster_1 = [
[d for d in dots if d[1] > 8],
[s for s in stars if s[1] > 8]
]

cluster_2 = [
[d for d in dots if d[1] < 8],
[s for s in stars if s[1] < 8]
]
clusters = [cluster_1, cluster_2]

min_clus = min(dist(center(cl[0]), s) for cl in clusters for s in cl[1])
max_clus = max(dist(center(cl[0]), s) for cl in clusters for s in cl[1])

print(min_clus*10_000, max_clus*10_000)