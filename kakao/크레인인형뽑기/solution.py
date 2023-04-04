from collections import deque

def solution(board, moves):
    answer = 0
    rows = len(board); cols = len(board[0])
    stk = deque()
    for col in moves:
        for row in range(rows):
            if board[row][col-1] != 0:
                doll = board[row][col-1]
                board[row][col-1] = 0
                if stk and stk[0] == doll:
                    stk.popleft()
                    answer += 2
                else:
                    stk.appendleft(doll)
                break
                    
    return answer
