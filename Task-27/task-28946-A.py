from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'./files/27_A_28946 (1).txt') as file:
    dots = [list(map(float, i.replace(',','.').split())) for i in file]

eps = 1
clusters = []
while dots:
    cluster = [dots.pop()]
    for dot in cluster:
        for d in dots.copy():
            if eps > dist(dot, d):
                cluster.append(d)
                dots.remove(d)
    clusters.append(cluster)

max_cluster = max(clusters, key=lambda x: len(x))
sum_max = sum(center(max_cluster)[1] > dot[1] for dot in max_cluster)

dist_centers = abs(center(clusters[0])[0]) - abs(center(clusters[1])[0])

print(sum_max, dist_centers*10_000)

##################################################3

with open(r'./files/27_B_28946 (1).txt') as file:
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

min_cluster = min(clusters, key=len)
center_min = center(min_cluster)

cnt_center_min = [1 for n in min_cluster if -0.9 <= (n[0] - center_min[0]) <= 0.9 and -0.9 <= (n[1] - center_min[1]) <= 0.9]

centers_2 = sorted([len(cluster), center(cluster)] for cluster in clusters)
ceneters3 = [centers_2[1][1], centers_2[2][1]]

print(sum(cnt_center_min))
print((ceneters3[0][1] - ceneters3[1][1])*10_000)