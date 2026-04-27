from math import dist

def anticenter(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return max(res)[1]

with open(r'./files/27.19.A_20497.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

eps = 0.4
clusters = []

while dots:
    cluster = [dots.pop()]
    for dot in cluster:
        for d in dots.copy():
            if dist(dot, d) < eps:
                cluster.append(d)
                dots.remove(d)
    if len(cluster) > 4:
        clusters.append(cluster)

centers = [anticenter(cluster) for cluster in clusters]

print((centers[0][0] + centers[1][0] + centers[2][0]) / 3 * 10000)
print((centers[0][1] + centers[1][1] + centers[2][1]) / 3 * 10000)

with open(r'./files/27.19.B_20497.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

eps = 5
clusters = []

while dots:
    cluster = [dots.pop()]
    for dot in cluster:
        for d in dots.copy():
            if dist(dot, d) < eps:
                cluster.append(d)
                dots.remove(d)
    if len(cluster) > 4:
        clusters.append(cluster)

centers = [anticenter(cluster) for cluster in clusters]

print((centers[0][0] + centers[1][0] + centers[2][0] + centers[3][0] + centers[4][0]) / 5 * 10000)
print((centers[0][1] + centers[1][1] + centers[2][1] + centers[3][1] + centers[4][1]) / 5 * 10000)
