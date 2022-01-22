H, W, X, Y = map(int, input().split())
m = []
answer = [[0] * W for _ in range(H)]
for r in range(H + X):
    m.append(list(map(int, input().split())))

for h in range(H):
    for w in range(W):
        if (h < H and w < Y) or (h < X and w < W):
            answer[h][w] = m[h][w]

for h in range(X, H):
    for w in range(Y, W):
        answer[h][w] = m[h][w] - answer[h-X][w-Y]

for r in answer:
    print(' '.join(map(str, r)))

# 2 4 0 3
# 1 2 3 5 2 3 4
# 5 6 7 13 6 7 8

# 2 4 1 0
# 1 2 3 4
# 6 8 10 12
# 5 6 7 8

# 2 2 1 0
# 1 2
# 4 6
# 3 4
