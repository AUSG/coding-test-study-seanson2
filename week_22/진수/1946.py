import math
import sys
sys.stdin = open('../input.txt')
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    memos = [N+1 for _ in range(N + 1)]

    for n in range(N):
        score1, score2 = map(int, input().split())
        memos[score1] = score2

    answer = N

    for i in range(1, N+1):
        m = min(memos[i-1], memos[i])
        if m == memos[i-1]:
            answer -= 1
        memos[i] = m

    print(answer)