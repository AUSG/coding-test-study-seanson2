from sys import stdin
input = stdin.readline

from heapq import *

for _ in range(int(input())):
    visits = [False] * 1000000
    ai_id = 0

    min_heap = []
    max_heap = []
    for _ in range(int(input())):
        cmd, n = input().split()
        n = int(n)

        if cmd == 'I':
            heappush(min_heap, (n, ai_id))
            heappush(max_heap, (-n, ai_id))
            ai_id += 1

        else:
            if n < 0:
                visit = True
                while visit and min_heap:
                    number, id = heappop(min_heap)
                    visit = visits[id]
                    visits[id] = True
            else:
                visit = True
                while visit and max_heap:
                    number, id = heappop(max_heap)
                    visit = visits[id]
                    visits[id] = True
    visit_all = True

    for v in visits[:ai_id]:
        visit_all = v
        if not visit_all:
            break
    if visit_all:
        print('EMPTY')
    else:
        visit = True
        while visit and max_heap:
            number, id = heappop(max_heap)
            visit = visits[id]

        M = number

        visit = True
        while visit and min_heap:
            number, id = heappop(min_heap)
            visit = visits[id]
        m = number

        print(-M, m)


