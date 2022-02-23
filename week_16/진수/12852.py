N = int(input())
dp = [(0, 0) for _ in range(N+1)]

for n in range(2, N+1):
    cand = [(dp[n-1][0] + 1, n-1)]
    if n % 3 == 0: cand.append((dp[n // 3][0] + 1, n // 3))
    if n % 2 == 0: cand.append((dp[n // 2][0] + 1, n // 2))
    dp[n] = min(cand)

print(dp[-1][0])
answer = [N]
while True:
    a = dp[answer[-1]][1]
    if a == 0: break
    answer.append(a)
print(' '.join(map(str, answer)))