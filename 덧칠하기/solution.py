from collections import deque

def solution(n, m, section):
    answer = 0
    section = deque(section)
    s = None
    while section:
        if not s:
            s = section.popleft()
            answer += 1
        if not section:
            break
        if s < section[0] < s + m:
            section.popleft()
        else:
            s = None
    return answer
