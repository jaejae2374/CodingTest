from collections import defaultdict, deque
import sys 
sys.setrecursionlimit(10**9)

def dfs(departure, graph, visited, path):
    for destination in graph[departure]:
        if visited[f"{departure},{destination}"]!=0:
            visited[f"{departure},{destination}"]-=1
            path.append(destination)
            result, path_ = dfs(destination, graph, visited, path)
            if set(result.values())!={0}:
                visited[f"{departure},{destination}"]+=1
                path.pop()
            else:
                return result, path_
    return visited, path

def solution(tickets):
    graph = defaultdict(list)
    visited = {}
    path = deque()
    for s, e in tickets:
        graph[s].append(e)
        graph[s].sort()
        if visited.get(f"{s},{e}", -1)<0:
            visited[f"{s},{e}"]=1
        else:
            visited[f"{s},{e}"]+=1
    path.append("ICN")
    _, path = dfs("ICN", graph, visited, path)
    
    return list(path)
