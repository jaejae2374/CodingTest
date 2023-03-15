from collections import Counter

def check(b, row, col, board):
    h = 0
    if col-1>=0 and board[row][col-1] == b:
        h += 1
    if col+1<3 and board[row][col+1] == b:
        h += 1
    if h == 2:
        return True
    
    v = 0
    if row-1>=0 and board[row-1][col] == b:
        v += 1
    if row+1<3 and board[row+1][col] == b:
        v += 1
    if v == 2:
        return True
    
    x = 0
    if row-1>=0 and col-1>=0 and board[row-1][col-1] == b:
        x += 1
    if row+1<3 and col+1<3 and board[row+1][col+1] == b:
        x += 1
    if x == 2:
        return True
        
    y = 0
    if row-1>=0 and col+1<3 and board[row-1][col+1] == b:
        y += 1
    if row+1<3 and col-1>=0 and board[row+1][col-1] == b:
        y += 1
    if y == 2:
        return True
    
    return False
    
def solution(board):
    # case 1. X가 O 보다 많을 때
    # case 1. O가 X 보다 두개 이상 많을 때
    cnt = Counter()
    for row in board:
        cnt += Counter(row)
    if not (0 <= cnt.get("O", 0) - cnt.get("X", 0) < 2):
        return 0
    
    # case 2. O가 이겼는데 o - x 가 1이 아닐 때
    # case 2. X가 이겼는데 o - x 가 0이 아닐 때
    # case 2. 이기는 상황이 두개 이상일 때
    cases = []
    winner = None
    for row in range(3):
        for col in range(3):
            b = board[row][col]
            if b == ".": continue
            isWinner = check(b, row, col, board)
            if isWinner:
                winner = b
                cases.append(winner)
    cases = Counter(cases)
    if cases.get("O", 0) and cases.get("X", 0):
        return 0
    if winner == "O" and cnt.get("O", 0) - cnt.get("X", 0) != 1:
        return 0
    if winner == "X" and cnt.get("O", 0) - cnt.get("X", 0) != 0:
        return 0
    return 1
