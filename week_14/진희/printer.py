from collections import deque


def solution(priorities, location):
    priorities = deque(priorities)
    answer = 0
    while (True):
        m = max(priorities)
        v = priorities.popleft()

        if(m == v):
            answer += 1
            if(location == 0):
                break
            else:
                location -= 1
        else:
            priorities.append(v)
            if(location == 0):
                location = len(priorities) - 1
            else:
                location -= 1
    return answer


priorities = [1, 1, 9, 1, 1, 1]
location = 0
print(solution(priorities, location))
