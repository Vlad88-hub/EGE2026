from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'./files/27_A_29076.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',','.').split()
        dots.append(list(map(float, [x, y])))
        if data[1] == '2':
            stars.append(list(map(float, [x, y])))

cluster_1 = [dot for dot in dots if dot[1] < 8]
cluster_2 = [dot for dot in dots if dot[1] > 8]

cnt_stars_cluster1 = [1 for s in stars if s in cluster_1]
cnt_stars_cluster2 = [1 for s in stars if s in cluster_2]

print(center(cluster_2)[0]*10_000)
print(center(cluster_1)[1]*10_000)