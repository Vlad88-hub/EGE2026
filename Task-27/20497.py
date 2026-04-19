from math import dist

def anticenter(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return max(res)[1]

with open(r'./files/27.19.A_20497.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

cluster_A_1 = [dot for dot in dots if dot[0] < 0 and dot[1] < 0]
cluster_A_2 = [dot for dot in dots if dot[0] > 0.5 and -6 < dot[1] < 0]
cluster_A_3 = [dot for dot in dots if dot[0] > -1 and 6 > dot[1] > 0]

center_A_1 = anticenter(cluster_A_1)
center_A_2 = anticenter(cluster_A_2)
center_A_3 = anticenter(cluster_A_3)

print((center_A_1[0] + center_A_2[0] + center_A_3[0]) / 3 * 10_000)
print((center_A_1[1] + center_A_2[1] + center_A_3[1]) / 3 * 10_000)

with open(r'./files/27.19.B_20497.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

cluster_B_1 = [dot for dot in dots if dot[0] < -35 and dot[1] < 35]
cluster_B_2 = [dot for dot in dots if -10 > dot[0] > -25 and dot[1] < 35]
cluster_B_3 = [dot for dot in dots if dot[0] > 0 and dot[1] < 35]
cluster_B_4 = [dot for dot in dots if -20 > dot[0] > -40 and dot[1] > 35]
cluster_B_5 = [dot for dot in dots if dot[0] > -15 and dot[1] > 35]

center_B_1 = anticenter(cluster_B_1)
center_B_2 = anticenter(cluster_B_2)
center_B_3 = anticenter(cluster_B_3)
center_B_4 = anticenter(cluster_B_4)
center_B_5 = anticenter(cluster_B_5)

print((center_B_1[0] + center_B_2[0] + center_B_3[0] + center_B_4[0] + center_B_5[0]) / 5 * 10_000)
print((center_B_1[1] + center_B_2[1] + center_B_3[1] + center_B_4[1] + center_B_5[1]) / 5 * 10_000)