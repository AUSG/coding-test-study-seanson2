from sys import stdin

input= stdin.readline

import heapq

N, K = map(int, input().split())
jewelries = []
bags = []
for _ in range(N):
    m, v = map(int, input().split())
    jewelries.append((-v, m))
for _ in range(K):
    bags.append(int(input()))

# 가벼운 녀석 순으로 정렬
jewelries.sort(key=lambda j: j[1])
bags.sort()
# 몇 번째 보석을 담을 차례인가.
cur = 0
pq = []
s = 0
for bag in bags:
    while cur < len(jewelries) and jewelries[cur][1] <= bag:
        heapq.heappush(pq, jewelries[cur])
        cur += 1
    if pq:
        s = s - heapq.heappop(pq)[0]


print(s)