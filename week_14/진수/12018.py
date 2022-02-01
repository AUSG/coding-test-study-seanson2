N, M = map(int, input().split())
lectures = []
answer = 0
s = 0
for _ in range(N):
    p, l = map(int, input().split())
    ms = list(map(int, input().split()))
    ms.sort(reverse=True)
    if p < l:
        lectures.append(1)
    else:
        lectures.append(ms[l-1])

lectures.sort()

for l in lectures:
    if l + s <= M:
        s += l
        answer += 1
    else:
        break
# print(lectures)
print(answer)
