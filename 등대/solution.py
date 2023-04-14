from collections import defaultdict
import sys
sys.setrecursionlimit(10**5)

def dfs(cur, graph, visited):
    visited[cur] = 1
    nxt_nodes = [adj_n for adj_n in graph[cur] if visited[adj_n]==0]

    active, inactive = 1, 0
    if not nxt_nodes: 
        return active, inactive

    for nxt in nxt_nodes:
        nxt_active, nxt_inactive = dfs(nxt, graph, visited)
        active += min(nxt_active, nxt_inactive)
        inactive += nxt_active
    return active, inactive

def solution(n, lighthouse):
    graph = defaultdict(set)
    for a, b in lighthouse:
        graph[a].add(b)
        graph[b].add(a)

    visited = [0]*(n+1)
    answer = dfs(1, graph, visited)
    return min(answer)
