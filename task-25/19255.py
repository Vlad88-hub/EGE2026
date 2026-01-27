from fnmatch import fnmatch

for N in range(5401037 - 5401037 % 18579, 10**10, 18579):
    if fnmatch(str(N), '54?1?3*7') and N % 18579 == 0:
        print(N, N // 18579)