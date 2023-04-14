import heapq
from collections import defaultdict
from math import inf

def solution(alp, cop, problems):
    
    problems += [[0, 0, 1, 0, 1], [0, 0, 0, 1, 1]]
    
    def put(t, key):
        if t < dp[key]:
            dp[key] = t
            heapq.heappush(q, (t, key))
            
    dp = defaultdict(lambda: inf)
    dp[(alp, cop)] = 0
    
    algoal = max(i[0] for i in problems)
    cogoal = max(i[1] for i in problems)
    
    q = [(0, (alp, cop))]
    while q[0][1][0] < algoal or q[0][1][1] < cogoal:
        t, (cal, cco) = heapq.heappop(q)
        for alreq, coreq, alrwd, corwd, cost in problems:
            if cal >= alreq and cco >= coreq:
                put(t+cost, (min(cal+alrwd, 150), min(cco+corwd, 150)))
    return q[0][0]
