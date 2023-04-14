from itertools import permutations
from collections import defaultdict
import copy
from math import inf

answer = inf
def solution(board, r, c):

    def dfs(case, start, idx, total, board):
        global answer
        if len(case) <= idx:
            return total
        if answer <= total:
            return inf
        node = case[idx]
        graph[node].sort(key=lambda x: abs(x[0]-start[0])+abs(x[1]-start[1]))
        ans1 = 0; ans2 = 0; start1 = start; start2 = start
        board1 = copy.deepcopy(board); board2 = copy.deepcopy(board)
        for i in range(2):
            node1 = graph[node][i]
            node2 = graph[node][-i-1]
            ans1 += min(check_row(start1[0], node1[0], start1[1], board)+check_col(start1[1], node1[1], node1[0], board), check_col(start1[1], node1[1], start1[0], board)+check_row(start1[0], node1[0], node1[1], board))
            start1 = node1
            ans2 += min(check_row(start2[0], node2[0], start2[1], board)+check_col(start2[1], node2[1], node2[0], board), check_col(start2[1], node2[1], start2[0], board)+check_row(start2[0], node2[0], node2[1], board))
            start2 = node2
            board1[node1[0]][node1[1]] = 0
            board2[node2[0]][node2[1]] = 0
        return min(dfs(case, start1, idx+1, total+ans1+2, board1), dfs(case, start2, idx+1, total+ans2+2, board2))
    
    def check_col(c1, c2, r, board):
        d = abs(c2-c1)
        if d==0: return 0
        elif d==1: return 1
        elif d==3: 
            tmp = 1
            if board[r][1]!=0: tmp+=1
            if board[r][2]!=0: tmp+=1
            return tmp
        else:
            if c2>c1: f1, f2, f3 = 3, 2, 1 
            else: f1, f2, f3 = 0, 1, 2
            if c2==f1:
                if board[r][f2]!=0: return 2
                else: return 1
            else:
                if board[r][f2]!=0 and board[r][f3]==0: return 1
                else: return 2

    def check_row(r1, r2, c, board):
        d = abs(r2-r1)
        if d==0: return 0
        elif d==1: return 1
        elif d==3: 
            tmp = 1
            if board[1][c]!=0: tmp+=1
            if board[2][c]!=0: tmp+=1
            return tmp
        else:
            if r2>r1: f1, f2, f3 = 3, 2, 1 
            else: f1, f2, f3 = 0, 1, 2
            if r2==f1:
                if board[f2][c]!=0: return 2
                else: return 1
            else:
                if board[f2][c]!=0 and board[f3][c]==0: return 1
                else: return 2

    def get_graph(rows, cols):
        cnt = 0; graph = defaultdict(list)
        for i in range(rows):
            for j in range(cols):
                if board[i][j]>0:
                    graph[board[i][j]].append((i, j))
                    cnt+=1
        return graph, cnt//2
    
    graph, cnt = get_graph(len(board), len(board[0]))
    cases = permutations(range(1, cnt+1), cnt)
    global answer
    
    for case in cases:
        board_ = copy.deepcopy(board)
        start = (r, c)
        ans = dfs(case, start, 0, 0, board_)
        if answer > ans:
            answer=ans
        
    return answer

