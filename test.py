from collections import defaultdict, deque
from math import inf

def solution(land):
    def bfs(i, j, rows, cols, land):
        oils = 0
        queue = deque()
        queue.append([i, j])
        tops = defaultdict(lambda: inf)
        while queue:
            x, y = queue.popleft()
            land[x][y] = 0
            tops[y] = min(tops[y], x)
            oils+=1
            # 상
            if x>=1 and land[x-1][y]==1:
                queue.append([x-1, y])
            # 하
            if x<rows-1 and land[x+1][y]==1:
                queue.append([x+1, y])
            # 좌
            if y>=1 and land[x][y-1]==1:
                queue.append([x, y-1])
            # 우
            if y<cols-1 and land[x][y+1]==1:
                queue.append([x, y+1])
        for y, x in tops.items():
            land[x][y] = oils
            
        return land
            
    answer = 0
    visited = defaultdict(bool)
    cols = len(land[0]); rows = len(land)
    visited = defaultdict(bool)
    for j in range(cols):
        oils = 0
        for i in range(rows):
            if land[i][j]==1 and visited[f"{i},{j}"]==False:
                land = bfs(i, j, rows, cols, land)
                visited[f"{i},{j}"] = True
            if land[i][j]>0:
                print(i, j)
                oils+=land[i][j]
        answer = max(answer, oils)
        print(f"oils: {oils}")
        print("=====================")
        
    return answer
solution(([[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]))