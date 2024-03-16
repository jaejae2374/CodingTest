from itertools import combinations
from collections import deque
from math import inf
import heapq
def solution(k, n, reqs):
    answer = 0
    mentors = deque()
    cases = combinations(range(1, n), k-1)
    works = {}
    for case in cases:
        before = 0; tmp = [0]*k
        for i, c in enumerate(case):
            tmp[i]=(c-before)
            before = c
        tmp[-1] = n-before
        mentors.append(tmp)
    answer = inf
    for mentor in mentors:
        waits = 0
        for i in range(k):
            works[i+1] = [0]*mentor[i]
        for rs, rt, rk in reqs:
            min_work = heapq.heappop(works[rk])
            if min_work<=rs:
                min_work=rs+rt
            else:
                waits+=min_work-rs
                min_work+=rt
            heapq.heappush(works[rk], min_work)
        answer = min(answer, waits)
    return answer
