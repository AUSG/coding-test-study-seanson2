from math import floor, ceil
import math
N = int(input())
an = [math.inf] * (N+1)
points = []
n = 1
while True:
    tmp = (n ** 3 + 3 * (n ** 2) + 2 * n) / 6
    if N < tmp: break
    if tmp == floor(tmp):
        an[floor(tmp)] = 1
        points.append(floor(tmp))
        # print(n, tmp)
    n += 1

for n in range(1, N+1):
    if an[n] != 1:
        for p in points:
            if p <= n:
                an[n] = min(an[n], 1 + an[n - p])

# print(an)
print(an[-1])
