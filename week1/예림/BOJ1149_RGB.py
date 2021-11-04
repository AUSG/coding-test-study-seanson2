# RGB

# n : 집의 수
n = int(input())

# 초기세팅 0으로 다 깔아놓거라
dp = [[0, 0, 0] for _ in range(n)]

for i in range(n):
    # 우선 먼저 입력받음
    cost = list(map(int, input().split()))

    # 첫 입력인 경우
    if i == 0:
        dp[0] = cost
    else:
        # 점화식 넣어주세효
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[2]

# dp 리스트의 n-1번째에 있는 누적된 RGB 비용 중 가장 최소 값을 출력한다.
print(min(dp[n-1]))