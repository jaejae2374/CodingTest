from collections import deque

def solution(queue1, queue2):
    s = sum(queue1 + queue2)
    if s%2 != 0:
        return -1
    s = int(s/2)
    
    s1 = sum(queue1); s2 = sum(queue2); std = 3*len(queue1)
    q1 = deque(queue1); q2 = deque(queue2)
    
    answer = 0
    while s != s1:
        if answer > std: return -1
        if s1 > s2:
            p = q1.popleft()
            s1 -= p
            s2 += p
            q2.append(p)
        else:
            p = q2.popleft()
            s2 -= p
            s1 += p
            q1.append(p)
        answer += 1
    return answer
