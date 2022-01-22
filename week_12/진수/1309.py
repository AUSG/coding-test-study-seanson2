N = int(input())
a = 3
b = 7
if N == 1: print(a)
elif N == 2: print(b)
else:
    for n in range(N-2):
        a, b = b, 2*b + a
    print(b % 9901)
