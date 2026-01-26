from fnmatch import fnmatch

for N in range(30157 - 30157 % 2023, 10**8, 2023):
    if fnmatch(str(N), '3?1*57') and N % 2023 == 0:
        print(N, N // 2023)