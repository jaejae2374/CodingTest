from collections import deque, defaultdict
from math import inf

def solution(board):
    
    def check_goal(r, c):
        cnt = 0
        if board[r+1][c]=='D': cnt+=1
        if board[r-1][c]=='D': cnt+=1
        if board[r][c-1]=='D': cnt+=1
        if board[r][c+1]=='D': cnt+=1
        if cnt==4 or cnt==0: return False
        else: return True
    
    # D로 감싸기
    rows = len(board)
    cols = len(board[0])
    for i, row in enumerate(board):
        board[i] = "D"+row+"D"
    board = ["D"*(cols+2)] + board + ["D"*(cols+2)] 

    # Graph 만들기
    start = (0, 0); finish = (0, 0)
    rows += 2; cols += 2
    points = deque()
    cnt = 0
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == "R":
                start = (row, col)
                board[row] = board[row].replace("R", ".")
            elif board[row][col] == "G":
                finish = (row, col)
                board[row] = board[row].replace("G", ".")
            if board[row][col] != "D":
                cnt += 1
                points.append((row, col))
                
    if not check_goal(finish[0], finish[1]): return -1
    
    graph = defaultdict(deque)
    
    for r, c in points:
        node = f"{r},{c}"
        
        # 오른쪽 갈 수 있는 . 체크
        for i in range(c+1, cols):
            if board[r][i]=='D':
                break
        graph[node].append(f"{r},{i-1}")
                
        # 왼쪽 갈 수 있는 . 체크
        for i in range(c-1, -1, -1):
            if board[r][i]=='D':
                break
        graph[node].append(f"{r},{i+1}")
                
        # 위쪽 갈 수 있는 . 체크
        for i in range(r-1, -1, -1):
            if board[i][c]=='D':
                break
        graph[node].append(f"{i+1},{c}")
                
        # 아래쪽 갈 수 있는 . 체크
        for i in range(r+1, rows):
            if board[i][c]=='D':
                break
        graph[node].append(f"{i-1},{c}")

    # bfs로 R부터 G까지 최단거리 찾기
    start = f"{start[0]},{start[1]}"; finish = f"{finish[0]},{finish[1]}"
    bfs = deque([start])
    distances = defaultdict(lambda: inf)
    distances[start] = 0
    while bfs:
        node = bfs.popleft()
        for n in graph[node]:
            if distances[n] > distances[node]+1:
                distances[n] = distances[node]+1
                bfs.append(n)
    if distances[finish] < inf:
        return distances[finish]
    else:
        return -1
