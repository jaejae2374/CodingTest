from collections import deque

def solution(ingredient):
    ingredient = deque(ingredient)
    q = deque()
    answer = 0
    while ingredient:
        q.append(ingredient.popleft())
        if len(q) >= 4:
            if [q[-4], q[-3], q[-2], q[-1]] == [1, 2, 3, 1]:
                answer += 1
                for _ in range(4):
                    q.pop()
            
    return answer
