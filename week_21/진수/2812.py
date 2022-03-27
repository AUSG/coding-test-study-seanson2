import sys
sys.stdin = open('../input.txt')
input = sys.stdin.readline

N, K = map(int, input().split())
number = list(map(int, input().strip()))
number.append(10)
# 내 뒤에 있는 수 중 해당 숫자가 처음 등장하는 인덱스
MAX = 500001
# 1, 2, ..., 9까지의 숫자들이 자신보다 큰 수가 등장하는 가장 작은 인덱스들을 저장하기 위함
# 9는 0이 아닌 10을 바라보도록해서 9보다 큰 1의 자리는 없음을 나타내기 위해 10을 더미로 넣는다.
memos = [[MAX for _ in range(11)] for _ in range(N+1)]

for i in range(N-1, -1, -1):
    for j in range(10):
        memos[i][j] = memos[i+1][j]
    memos[i][number[i+1]] = i + 1

answer = []

def getFirstBigger(idx):
    n1 = number[idx]
    found = False

    return min(memos[idx][n1+1:])

for i in range(N):
    # 여태까지 살려놓은 것 개수 + (나보다 큰애부터 살릴 수 있는 것 개수)
    fb = getFirstBigger(i)
    if (fb != MAX and len(answer) + N - fb < N-K) or (fb == MAX and len(answer) < N-K ):
        answer.append(number[i])

print(''.join(map(str, answer)))