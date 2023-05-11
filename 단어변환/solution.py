from collections import defaultdict
from math import inf
import heapq

def dijkstra(start, end, graph):
    distances = defaultdict(lambda: inf)
    distances[start]=0
    paths = []
    heapq.heappush(paths, [0, start])
    while paths:
        d, node = heapq.heappop(paths)
        if distances[node] < d:
            contunue
        for next_node in graph[node]:
            if distances[next_node] > d+1:
                distances[next_node] = d+1
                heapq.heappush(paths, [distances[next_node], next_node])
    return distances[end]
                
def check(s1, s2):
    cnt = 0
    for c1, c2 in zip(list(s1), list(s2)):
        if c1 != c2:
            cnt+=1
        if cnt>1:
            return False
    if cnt==1: return True
    return False

def solution(begin, target, words):
    if target not in words: return 0
    graph = defaultdict(list)
    fin = len(words)
    cnt = 0
    std = begin
    while True:
        for word in words:
            if check(std, word):
                graph[std].append(word)
        if cnt==fin: break
        std = words[cnt]
        cnt+=1
    return dijkstra(begin, target, graph)
