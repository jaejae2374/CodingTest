from datetime import datetime, timedelta
from collections import deque

def solution(plans):
    answer = []
    plans = deque(sorted(plans, key=lambda x: x[1]))
    stk = deque()
    while plans:
        p1 = plans.popleft()
        if not plans:
            stk.append(p1)
            break
        p2 = plans[0]
        finish = datetime.strptime(p1[1], "%H:%M") + timedelta(minutes=int(p1[2]))
        start = datetime.strptime(p2[1], "%H:%M")
        if finish > start:
            m = (finish-start).seconds//60
            p1[1] = p2[1]
            p1[2] = m
            stk.append(p1)
        else:
            m = (start-finish).seconds//60
            answer.append(p1[0])
            while stk:
                s = stk[-1]
                if s[2] > m:
                    s[2] -= m
                    break
                else:
                    m -= s[2]
                    answer.append(stk.pop()[0])
                    if m == 0: break
    if stk:
        for _ in range(len(stk)):
            answer.append(stk.pop()[0])
    return answer
