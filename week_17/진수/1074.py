N, R, C = map(int, input().split())
def rec(r, c, num, size):
    if r == R and c == C and size == 1:
        print(num)
    if size == 1:
        return num + 1
    
    ns = size // 2
    if r <= R < r + ns and c <= C < c + ns:
        return rec(r, c, num, ns)
    elif r <= R < r + ns and c + ns <= C < c + size:
        return rec(r, c + ns, num + ns ** 2, ns)
    elif r + ns <= R < r + size and c <= C < c + ns:
        return rec(r + ns, c, num + 2 * ns ** 2, ns)
    else:
        return rec(r + ns, c + ns, num + 3 * ns ** 2, ns)

rec(0, 0, 0, 2 ** N)
