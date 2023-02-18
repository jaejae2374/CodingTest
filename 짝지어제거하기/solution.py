from collections import deque

def solution(s):
    stk = deque()
    s = deque(s)
    while s:
        ch = s.popleft()
        if stk and stk[-1] == ch:
            stk.pop()
        else:
            stk.append(ch)
    if stk:
        return 0
    else: 
        return 1
