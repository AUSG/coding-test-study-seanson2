import sys
from sys import stdin
sys.setrecursionlimit(1000000)
#stdin = open('input.txt')
input = stdin.readline

N = int(input())
# 한 칸은 더미
tree = [dict() for _ in range(N+1)]
# 각 노드들이 갖는 weight들
# 0, 0은 sum하기 편하라고 둔 dummy
weights = [[0, 0] for _ in range(N+1)]
for _ in range(N-1):
    p, c, w = map(int, input().split())
    # 부모, 자식
    tree[p][c] = w

def dfs(node):
    # 비어있다면
    if not tree[node]:
        return 0

    for child, weight in tree[node].items():
        weights[node].append(dfs(child) + weight)

    return max(weights[node])

dfs(1)

for weight_list in weights:
    weight_list.sort(reverse=True)

answer = 0
for weight_list in weights:
    answer = max(answer, sum(weight_list[:2]))

print(answer)

