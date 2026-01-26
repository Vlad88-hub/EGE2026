from fnmatch import fnmatch

for N in range(1021394 - 1021394, 10**10, 2023):
    if fnmatch(str(N), '1?2139*4') and N % 2023 == 0:
        print(N, N // 2023)