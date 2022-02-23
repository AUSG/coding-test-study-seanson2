from sys import stdin
input = stdin.readline

from heapq import *

N = int(input())
lectures = [list(map(int, input().split())) for _ in range(N)]

# 시작 시간이 빠른 순, 끝나는 시간은 상관 없어!
lectures.sort()

line = 1
# 각 라인의 끝나는 시간에 대한 min heap
end_min_heap = [(0, line)]

for lecture in lectures:
    end_min = heappop(end_min_heap)
    if lecture[0] < end_min[0]:
            heappush(end_min_heap, end_min)
            line += 1
            heappush(end_min_heap, (lecture[1], line))
    else:
        heappush(end_min_heap, (lecture[1], end_min[1]))

print(line)

