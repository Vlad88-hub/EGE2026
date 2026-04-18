with open(r'.\files\26.2_19727.txt') as file:
    V, N = map(int, file.readline().split())
    cans = [int(i) for i in file]

cans = sorted(cans)
max_list_can = []

for can in cans:
    if sum(max_list_can) + can < V:
        max_list_can.append(can)

max_list_can =max_list_can[:-1]
free_space = V - sum(max_list_can)

cnt = 0
for n in cans:
    if n > free_space:
        cnt += 1

print(len(max_list_can) + 1 ,sum(i > free_space for i in cans), cnt)


# matches = ['1232', '132']
#
# ans = 0
# for match in matches:
#     if sum(map(int, match)) == 2024:
#         ans = max(ans, match)
#     else:
#         for l in range(0, len(match)):
#             for r in range(len(match), l, -1):
#                 new_match = match[l:r + 1].split('0')
#                 if sum(map(int, new_match)) == 2024:
#                     ans = max(ans, len(new_match))


# 6
data = '12zzzzz31zz2'

l = 0
r = 0
ans = 10**10
sum_str = 0
len_str = len(data)

while r != len_str or l != len_str - 1:
    if sum_str < 6:
        if data[r] in '0123456789': sum_str += int(data[r])
        r += 1
    else:
        if sum_str == 6: ans = min(ans, r - l)
        if data[l] in '0123456789': sum_str -= int(data[r])
        l += 1

print(ans)