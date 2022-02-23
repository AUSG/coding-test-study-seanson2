import math
import sys
from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
numbers = []
for _ in range(N):
    numbers.append(int(input()))

numbers.sort()

left = 0
right = 0

answer = sys.maxsize
while left <= right < N:
    a, b = numbers[left], numbers[right]
    if b - a < M:
        right += 1
    else:
        answer = min(answer, b - a)
        left += 1

print(answer)