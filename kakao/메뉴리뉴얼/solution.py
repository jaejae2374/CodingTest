from itertools import combinations
from collections import Counter

def solution(orders, course):
    l = []
    answer = []
    
    for c in course:
        tmp = []
        for order in orders:
            order = sorted(order)
            tmp += list(combinations(order, c))
        l.append(Counter(tmp))
    answer = []
    for counter in l:
        tmp = counter.most_common()
        if len(tmp) == 0: continue
        cnt = tmp[0][1]
        idx = 0
        while cnt > 1:
            if cnt == tmp[idx][1]:
                answer.append("".join(tmp[idx][0]))
                idx += 1
            else:
                break
        
    answer.sort()
    return answer
