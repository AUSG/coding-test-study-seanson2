# 빗물

# 입력을 받아 준다.
H, W = map(int, input().split())
block = list(map(int, input().split()))
answer = 0

# 맨 앞뒤를 제외한 for문을 돌면서 왼쪽과 오른쪽에서 최댓값을 찾는다.
for i in range(1, W-1):
    left = max(block[:i])
    right = max(block[i+1:])
    m = min(left, right)
    if block[i] < m:
        answer += m - block[i]

print(answer)