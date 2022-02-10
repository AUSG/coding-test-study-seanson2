from collections import deque


def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    answer = 0
    answer w, t = 0, deque([]), deque([])
    while(len(truck_weights) != 0 or len(w) != 0):
        answer += 1
        if(len(t) > 0):
            for i in range(len(t)):
                t[i] -= 1
            if (t[0] == 0):
                t.popleft()
                w.popleft()
        if(len(truck_weights) != 0):
            if(truck_weights[0] <= weight-sum(w)):
                pop = truck_weights.popleft()
                t.append(bridge_length)
                w.append(pop)
    return answer


bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]
print(solution(bridge_length, weight, truck_weights))
