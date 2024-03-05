from collections import deque

def solution(numbers):
    stack = deque()
    result = [-1] * len(numbers)
    stack.appendleft([numbers[0], 0])
    for i in range(1, len(numbers)):
        if stack[0][0]>=numbers[i]:
            stack.appendleft([numbers[i], i])
        else:
            while stack and stack[0][0]<numbers[i]:
                _, idx = stack.popleft()
                result[idx]=numbers[i]
            stack.appendleft([numbers[i], i])

    return result
