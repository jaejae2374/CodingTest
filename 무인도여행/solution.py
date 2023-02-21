from collections import deque

def solution(maps):
    answer = []; visited = {}
    rows = len(maps); cols = len(maps[0])
    
    for row in range(rows):
        for col in range(cols):
            if maps[row][col] != "X" and not visited.get(f"{row},{col}"):
                bfs = deque()
                bfs.append((row, col))
                foods = 0
                while bfs:
                    r, c = bfs.popleft()
                    if visited.get(f"{r},{c}"):
                        continue
                    foods += int(maps[r][c])
                    visited[f"{r},{c}"] = True
                    if r-1 >= 0 and not visited.get(f"{r-1},{c}") and maps[r-1][c] != "X":
                        bfs.append((r-1, c))
                    if r+1 < rows and not visited.get(f"{r+1},{c}") and maps[r+1][c] != "X":
                        bfs.append((r+1, c))
                    if c-1 >= 0 and not visited.get(f"{r},{c-1}") and maps[r][c-1] != "X":
                        bfs.append((r, c-1))
                    if c+1 < cols and not visited.get(f"{r},{c+1}") and maps[r][c+1] != "X":
                        bfs.append((r, c+1))
                answer.append(foods)
    if answer: 
        return sorted(answer)
    else:
        return [-1]
    