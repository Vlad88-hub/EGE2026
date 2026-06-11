from math import dist
from itertools import combinations

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[-1]

with open(r'./files/27_B_29081.txt') as file:
    dots = []
    stars = []
    for i in file:
        x,y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[1] in '89':
            stars.append(dots[-1])

stars_1 = [dot for dot in stars if dot[1] > 22]
stars_2 = [dot for dot in stars if 16 < dot[1] < 22]
stars_3 = [dot for dot in stars if 16 > dot[1]]
all_stars = [stars_1,stars_2,stars_3]

min_dist_stars = min(dist(s1, s2) for cl1, cl2 in combinations(all_stars, 2) for s1 in cl1 for s2 in cl2)

cl_dist = [dist(s1, s2) for cl1, cl2 in combinations(all_stars, 2) for s1 in cl1 for s2 in cl2]

print(min_dist_stars * 10_000, (sum(cl_dist)/len(cl_dist)) * 10_000)