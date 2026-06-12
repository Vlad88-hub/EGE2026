with open(r'../files/26.2_19727.txt') as file:
    M, N = map(int, file.readline().split())
    bids = [int(i) for i in file]

bids = sorted(bids)

max_bids = []
for bid in bids:
    if sum(max_bids) + bid <= M:
        max_bids.append(bid)

len_max_bids = len(max_bids)

cnt_bid = len_max_bids
for i in range(len_max_bids, len(bids)):
    if sum(max_bids[:-1]) + bids[i] <= M:
        cnt_bid += 1
        max_bids.pop()
        max_bids.append(bids[i])

print(len_max_bids, N - cnt_bid)