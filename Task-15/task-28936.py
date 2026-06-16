# def f(x, y):
#     return (x + y < A) or (5 * x < y) or (486 <= x)
#
# for A in range(0, 1000):
#     if all(f(x, y) for x in range(0, 1000) for y in range(0, 1000)):
#         print(A)
#         break

# (x * y < A)
# (5 * x >= y)
# (x < 486)

# больше большего
# x max == 485
# y max == 485 * 5
# => A = 485 * 5 * 485 + 1

print(485 * 5 * 485 + 1)