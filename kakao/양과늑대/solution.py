from collections import deque, defaultdict

def solution(info, edges):
    answer = 0
    tree = defaultdict(list)
    for parent, child in edges:
        tree[parent].append(child)
    bfs = deque([[0, tree[0], 1, 0]])
    while bfs:
        cur, moves, sheep, wolf = bfs.popleft()
        answer = max(answer, sheep)
        for i, node in enumerate(moves):
            if info[node] == 1:
                if sheep > wolf + 1:
                    bfs.append([node, moves[:i]+moves[i+1:]+tree[node], sheep, wolf+1])
            else:
                bfs.append([node, moves[:i]+moves[i+1:]+tree[node], sheep+1, wolf])
    
    return answer
