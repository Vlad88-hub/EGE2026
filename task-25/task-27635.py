from fnmatch import fnmatch

for i in range(1230056 - 1230056%171, 10**8, 171):
    if fnmatch(str(i), '1*23??56'):
        print(i, i//171)