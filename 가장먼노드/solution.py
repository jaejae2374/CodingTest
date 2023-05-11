from collections import defaultdict, deque
def solution(n, edge):
    answer = 0
    v = defaultdict(deque)
    for n1, n2 in edge:
        v[n1].append(n2)
        v[n2].append(n1)
    d = [30000]*n
    d[0] = 0
    bfs = deque([1])
    while bfs:
        node = bfs.popleft()
        for next_node in v[node]:
            if d[node-1]+1 < d[next_node-1]:
                bfs.append(next_node)
                d[next_node-1] = d[node-1]+1
    return d.count(max(d))
