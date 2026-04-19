from math import dist

def anticenter(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return max(res)[1]

with open(r'./files/27A_27590.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

eps = 1
clusters = []

while dots:
    cluster = [dots.pop()]
    for dot in cluster:
        for d in dots.copy():
            if dist(dot, d) < eps:
                cluster.append(d)
                dots.remove(d)
    clusters.append(cluster)

centers = [[len(cluster), anticenter(cluster)] for cluster in clusters]

max_center = max(centers)[1]
min_center = min(centers)[1]

print((max_center[0] + max_center[1])* 10000)
print((min_center[0] + min_center[1])* 10000)

with open(r'./files/27B_27590.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

eps = 1
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

centers = [[dist(anticenter(center), [0,0]),anticenter(center)] for center in clusters]

max_center = max(centers)[1]
min_center = min(centers)[1]

print(max_center[0]* 10_000, min_center[1] * 10_000)