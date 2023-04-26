from collections import deque, defaultdict

def check(start, end, graph, n):
    if not graph[start] or not graph[end]:
        return True
    dfs = deque(graph[start])
    visited = [0]*n
    visited[start]=1
    while dfs:
        node = dfs.popleft()
        visited[node]=1
        if node==end:
            return False
        for next_node in graph[node]:
            if visited[next_node]==0:
                dfs.appendleft(next_node)
    return True

def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    graph = defaultdict(list)
    cnt = 1
    idx = 0
    fin=len(costs)
    while cnt<n:
        n1, n2, c = costs[idx]
        if check(n1, n2, graph, n):
            answer+=c
            cnt+=1
            graph[n1].append(n2)
            graph[n2].append(n1)
        idx+=1
    return answer
