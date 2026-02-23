def f(start, cnt):
    if cnt == 15: return {start}
    return f(start + 10, cnt + 1) | f(start -5, cnt + 1)

print(len(f(1, 0)))

#########################################################################

def f(start, cnt):
    if cnt == 15:
        points.add(start)
        return
    f(start+10, cnt + 1)
    f(start - 5, cnt + 1)


points = set()
f(1, 0)
print(len(points))