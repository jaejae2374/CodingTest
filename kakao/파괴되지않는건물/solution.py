def solution(board, skill):
    answer = 0
    rows = len(board)
    cols = len(board[0])
    changed = [[0 for c in range(cols+1)] for r in range(rows+1)]
    
    for t, r1, c1, r2, c2, d in skill:
        if t == 1:
            d = -d
        changed[r1][c1] += d
        changed[r2+1][c1] -= d
        changed[r1][c2+1] -= d
        changed[r2+1][c2+1] += d
    for r in range(rows+1):
        for c in range(1, cols+1):
            changed[r][c] += changed[r][c-1]
    for c in range(cols+1):
        for r in range(1, rows+1):
            changed[r][c] += changed[r-1][c]
    for r in range(rows):
        for c in range(cols):
            board[r][c] += changed[r][c]
            if board[r][c] > 0:
                answer += 1
                
    return answer
