import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

from collections import defaultdict
from collections import deque

drdc = [
    [0, 1],
    [-1, 0],
    [0, -1],
    [1, 0],
]

R, C = 12, 6
board = [['.'] * C for _ in range(R)]
for r in range(R-1, -1, -1):
    board[r] = list(input().strip())


def bfs(r, c, _board, visit, bomb):
    block = _board[r][c]
    q = deque([(r, c)])
    visit[r][c] = True
    bomb_buffer = [(r, c)]

    while q:
        cr, cc = q.popleft()
        for dr, dc in drdc:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < R and 0 <= nc < C and not visit[nr][nc] and _board[nr][nc] == block:
                q.append((nr, nc))
                visit[nr][nc] = True
                bomb_buffer.append((nr, nc))

    if 4 <= len(bomb_buffer):
        for bomb_coord in bomb_buffer:
            bomb[bomb_coord[1]].append(bomb_coord[0])

answer = 0

while True:
    visit = [[False] * C for _ in range(R)]
    bomb = defaultdict(list)
    for r in range(R):
        for c in range(C):
            if board[r][c] != '.' and not visit[r][c]:
                bfs(r, c, board, visit, bomb)

    if bomb:
        for col, rows in bomb.items():
            rows.sort(reverse=True)
            for bomb_r in rows:
                for r in range(bomb_r, R):
                    if board[r][col] == '.': break

                    if r == R-1:
                        board[r][col] = '.'
                    else:
                        board[r][col] = board[r+1][col]
        answer += 1
        # for line in board[::-1]:
        #     print(line)
        # print()
        # print()
    else:
        break

print(answer)








