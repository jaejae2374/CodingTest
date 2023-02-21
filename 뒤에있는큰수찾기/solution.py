from collections import deque

def solution(numbers):
    
    answer = deque()
    answer.appendleft(-1)
    
    for i in range(-2, -len(numbers)-1, -1):
        before_big = answer[0]
        before = numbers[i+1]
        n = numbers[i]
        if n < before:
            answer.appendleft(before)
        elif n > before:
            if before_big == -1:
                answer.appendleft(before_big)
            else:
                for b in answer:
                    if b == -1:
                        answer.appendleft(-1)
                        break
                    if b > n:
                        answer.appendleft(b)
                        break
                else:
                    answer.appendleft(-1)
        else:
            answer.appendleft(before_big)
    
    return list(answer)
