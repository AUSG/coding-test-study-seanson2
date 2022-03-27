import sys
sys.stdin = open('../input.txt')
input = sys.stdin.readline

N = int(input())
numbers = sorted(list(map(int, input().split())))


# n보다 큰 수의 최소 인덱스
def upper_bound(n, left, right):
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] <= n:
            left = mid + 1
        else:
            right = mid - 1

    return left

# n 이상의 최소 인덱스
def lower_bound(n, left, right):
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] < n:
            left = mid + 1
        else:
            right = mid - 1

    return left

# 하나면 upper_bound와 lower_bound가 동일하다.
answer = 0

for i in range(N-2):
    a = numbers[i]
    left = i + 1
    right = N - 1

    while left < right:
        # print(a, numbers[left], numbers[right])
        s = a + numbers[left] + numbers[right]
        if s == 0:
            if numbers[left] == numbers[right]:
                c = (right - left + 1)
                answer += c * (c-1) // 2
                break
            else:
                left_ub = upper_bound(numbers[left], left, right)
                right_lb = lower_bound(numbers[right], left, right)
                answer += (left_ub - left) * (right - right_lb + 1)
                right = right_lb - 1
                left = left_ub
        elif s < 0:
            left += 1
        else:
            right -= 1


print(answer)
