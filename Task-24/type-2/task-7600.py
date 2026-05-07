with open(r'../files/24_7600.txt') as file:
    data = file.readline()

# ans = 0
# cnt = 0
# for i in range(len(data)-1):
#     if data[i:i+2] not in ['QR', 'RQ', 'QS', 'SQ', 'QQ', 'RS', 'SR', 'RS', 'RR', 'SS']:
#         cnt += 1
#     else:
#         ans = max(ans, cnt)
#         cnt = 0
#
# print(ans + 1)

cnt_1 = 0
ans_1 = 1
for i in range(len(data)-1):
    if data[i] not in 'QRS' or data[i+1] not in 'QRS':
        cnt_1 += 1
    else:
        ans_1 = max(ans_1, cnt_1)
        cnt_1 = 1

ans_1 = max(ans_1, cnt_1)

print(ans_1)