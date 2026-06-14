from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'./files/27_A_29074.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'Z':
            stars.append(dots[-1])

cluster_1 = [dot for dot in stars if dot[1] < 8]
cluster_2 = [dot for dot in stars if dot[1] > 8]
clusters = [cluster_1, cluster_2]

max_stars = len(max(clusters, key=lambda x: len(x)))
min_stars = len(min(clusters, key=lambda x: len(x)))

print(min_stars, max_stars)