from fnmatch import fnmatch

for n in range(89607090 - 89607090%9874, 10**10, 9874):
    if fnmatch(str(n),'89*6?7?9?'):
        print(n, n//9874)