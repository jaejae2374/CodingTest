from collections import deque

def solution(prices):
    stk = deque()
    answer = [len(prices) - i - 1 for i in range(len(prices))]
    for idx, price in enumerate(prices):
        if not stk:
            stk.append((idx, price))
        else:
            while stk and stk[-1][1] > price:
                tmp = stk.pop()
                answer[tmp[0]] = idx - tmp[0]
            stk.append((idx, price))
    return answer
