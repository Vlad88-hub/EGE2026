with open(r'.\files\26_16390.txt') as file:
    S, N = map(int, file.readline().split())
    gifts = [int(i) for i in file]

gifts = sorted(gifts)

ans = []
for gift in gifts:
    if sum(ans) + gift <= S:
        ans.append(gift)

ans = ans[:-1]
free_space = S - sum(ans)

print(len(ans) + 1, max([i for i in gifts if i <= free_space]))


    #     for gift in gifts[1:]:
    #         if int(S) - gift >= 0:
    #             cnt += 1
    #             S = int(S) - gift
    #             last_gift = gift
    #     ans.append([cnt, last_gift])

#
# print(max_cnt_ans, max_ans)

# f = open('26.txt')
# s, n = map(int, f.readline().split())
# kruz = sorted([int(x) for x in f])
# f.close()
#
# truck = []
# current_sum = 0
#
# for v in kruz:
#     if current_sum + v <= s:
#         current_sum += v
#         truck.append(v)
#     else:
#         break
#
# current_sum -= truck[-1]
#
# max_last = truck[-1]
# for v in kruz[::-1]:
#     if current_sum + v <= s:
#         max_last = v
#         break
#
# print(len(truck), max_last)