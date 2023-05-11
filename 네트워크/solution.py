from collections import defaultdict, deque
def dfs(node, graph, visited):
    visited[node] = True
    for next_node in graph[node]:
        if not visited[next_node]:
            visited = dfs(next_node, graph, visited)
    return visited

def solution(n, computers):
    answer = 0
    graph = defaultdict(deque)
    for i in range(len(computers)):
        for j in range(len(computers[0])):
            if i==j: continue
            if computers[i][j]==1:
                graph[i].append(j)
                graph[j].append(i)
    visited=[False]*n
    start=0
    while True:
        answer+=1
        visited = dfs(start, graph, visited)
        for i in range(n):
            if not visited[i]:
                start=i
                break
        else:
            break
    return answer
