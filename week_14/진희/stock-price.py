from collections import deque


def solution(prices):
    prices = deque(prices)
    answer = deque([])
    while(len(prices) != 0):
        count = 0
        pop = prices.popleft()
        for i in prices:
            count += 1
            if(i < pop):
                break

        answer.append(count)
    return answer


prices = [1, 2, 3, 2, 3]
print(solution(prices))
