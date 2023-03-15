from collections import defaultdict, deque

def get_map(roads):
    m = defaultdict(list)
    for road in roads:
        m[road[0]].append(road[1])
        m[road[1]].append(road[0])
    return m

def solution(n, roads, sources, destination):
    distances = [500000 for _ in range(n+1)]
    distances[destination] = 0
    maps = get_map(roads)
    bfs = deque([destination])
    while bfs:
        p1 = bfs.popleft()
        d = distances[p1]
        for p2 in maps[p1]:
            if d+1 < distances[p2]:
                distances[p2] = d+1
                bfs.append(p2)
    
    return [distances[i] if distances[i] != 500000 else -1 for i in sources]
