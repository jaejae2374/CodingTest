import heapq

def solution(priorities, location):
    ps = []
    results = []
    for idx, p in enumerate(priorities):
        ps.append((p, idx))
    while ps:
        t = ps.pop(0)
        if ps and heapq.nlargest(1, ps)[0][0] > t[0]:
            ps.append(t)
        else:
            results.append(t[1])
    return results.index(location) + 1
