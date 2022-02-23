from collections import deque

N = int(input())
pos_one = 0
zero = 0
negs, poses = [], []

for _ in range(N):
    n = int(input())
    if n <= -1:
        negs.append(n)
    elif n == 0:
        zero += 1
    elif n == 1:
        pos_one += 1
    else:
        poses.append(n)

poses.sort()
poses = deque(poses)
negs.sort(reverse=True)
negs = deque(negs)

s = 0
while poses:
    a = poses.pop()
    if not poses:
        s += a
        break
    b = poses.pop()
    s += a * b

while negs:
    a = negs.pop()
    if not negs:
        if zero != 0:
            zero -= 1
        else:
            s += a
        break
    b = negs.pop()
    s += a * b

s += pos_one

print(s)