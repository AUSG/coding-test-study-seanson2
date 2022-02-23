N = int(input())
flowers = []

for _ in range(N):
    # 시작 월, 시작 일, 끝 월, 끝 일
    start_m, start_d, end_m, end_d = map(int, input().split())
    # if (start_m == end_m and end_d < start_d) or end_m < start_m:
    #     raise RuntimeError("What?")
    flowers.append((start_m * 100 + start_d, end_m * 100 + end_d))

flowers.sort(key=lambda item: (item[0], -item[1]))

current, buf = 301, 0
answer = 0

cur = 0
while cur < N:
    if 1200 <= current: break
    start, end = flowers[cur]
    if start <= current:
        buf = max(buf, end)
        cur += 1
    else:
        if buf == 0:
            answer = -1
            break
        current = buf
        buf = 0
        answer += 1

if answer == -1:
    print(0)
else:
    if current < 1200:
        if 1200 <= buf:
            current = buf
            answer += 1

    if 1200 <= current:
        print(answer)
    else:
        print(0)
