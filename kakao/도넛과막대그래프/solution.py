from collections import defaultdict, deque
def solution(edges):
    O = 0; l = 0; OO = 0;
    graph = defaultdict(list)
    start = defaultdict(bool)
    started = defaultdict(bool)
    arrived = defaultdict(bool)
    for s, e in edges:
        graph[s].append(e)
        if started[s]:
            start[s]=True
        started[s]=True
        arrived[e]=True
    cnode = 0
    for node in start.keys():
        if not arrived[node]:
            cnode=node
            break
    for start_node in graph[cnode]:
        queue = deque()
        queue.append(start_node)
        visited = defaultdict(bool)
        isO = False; isOO = False
        while queue:
            node = queue.popleft()
            if visited[node]:
                isO=True
                continue
            visited[node] = True
            if len(graph[node])>1:
                isOO=True
            for next_node in graph[node]:
                queue.appendleft(next_node)
        if isOO:
            OO+=1
        elif isO:
            O+=1
        else:
            l+=1
    return [cnode, O, l, OO]
