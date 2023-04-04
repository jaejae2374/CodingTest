from collections import defaultdict

def solution(board):
    def check_goal(r, c):
        cnt = 0
        if r==rows-1 or board[r+1][c]=='D': cnt+=1
        if r==0 or board[r-1][c]=='D': cnt+=1
        if c==0 or board[r][c-1]=='D': cnt+=1
        if c==cols-1 or board[r][c+1]=='D': cnt+=1
        if cnt==4 or cnt==0: return False
        else: return True

    def dfs(r, c, visited, cnt):
        if visited[f"{r},{c}"]:
            return 0
        if r==finish[0] and c==finish[1]:
            return cnt+1
        tmp = []
        visited[f"{r},{c}"] = True
        if r!=rows-1 and board[r+1][c]!='D': 
            for i in range(r+1, rows):
                if board[i][c] == 'D':
                    break
            else:
                i+=1
            i-=1
            a = dfs(i, c, visited, cnt+1)
            print(i,c)
            if a:
                tmp.append(a)
        if r!=0 and board[r-1][c]!='D': 
            for i in range(r-1, -1, -1):
                if board[i][c] == 'D':
                    break
            else:
                i-=1
            i+=1
            a = dfs(i, c, visited, cnt+1)
            print(i,c)
            if a:
                tmp.append(a)
        if c!=0 and board[r][c-1]!='D': 
            for i in range(c-1, -1, -1):
                if board[r][i] == 'D':
                    break
            else:
                i-=1
            i+=1
            a = dfs(r, i, visited, cnt+1)
            print(r, i)
            if a:
                tmp.append(a)
        if c!=cols-1 and board[r][c+1]!='D': 
            for i in range(c+1, cols):
                if board[r][i] == 'D':
                    break
            else:
                i+=1
            i-=1
            a = dfs(r, i, visited, cnt+1)
            print(r, i)
            if a:
                tmp.append(a)
        visited[f"{r},{c}"] = False
        if tmp:
            return min(tmp)
        else:
            return 0
    start = (0, 0)
    finish = (0, 0)
    rows = len(board)
    cols = len(board[0])
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == "R":
                start = (row, col)
            elif board[row][col] == "G":
                finish = (row, col)
    if not check_goal(finish[0], finish[1]):
        return -1
    answer = dfs(start[0], start[1], defaultdict(bool), 0)
    if answer:
        return answer -1
    else:
        return -1

print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))