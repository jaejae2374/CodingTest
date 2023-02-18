from collections import deque

def solution(order):
    order = deque(order)
    answer = 0
    n = 1
    stk = deque([0])
    while order:
        need = order.popleft()
        if stk[-1] == need:
            answer += 1
            stk.pop()
        else:
            if n <= need:
                stk += [i for i in range(n, need)]
                n = need + 1
                answer += 1
            else:
                break
        
    return answer
