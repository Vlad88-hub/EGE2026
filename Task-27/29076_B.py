from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'./files/27_B_29076.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',','.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'Y':
            stars.append(list(map(float, [x, y])))

cluster_1 = [dot for dot in dots if dot[1] < 16]
cluster_2 = [dot for dot in dots if 22 > dot[1] > 16]
cluster_3 = [dot for dot in dots if 22 < dot[1]]

cnt_stars_cluster1 = [s for s in stars if s in cluster_1] #1
cnt_stars_cluster2 = [s for s in stars if s in cluster_2]#3
cnt_stars_cluster3 = [s for s in stars if s in cluster_3]#2

center_max = center(cluster_1)
center_min = center(cluster_2)

sum_1 = max(dist(dot, d) for dot in cluster_1 for d in cnt_stars_cluster1 if dot != d)
sum_2 = max(dist(dot, d) for dot in cluster_2 for d in cnt_stars_cluster2 if dot != d)
sum_3 = max(dist(dot, d) for dot in cluster_3 for d in cnt_stars_cluster3 if dot != d)
summ = [sum_1, sum_2, sum_3]

print(dist(center_max, center_min) * 10_000)
print(max(summ) * 10_000)
