from functools import reduce

def solution(n):
    answer = [[0]*i for i in range(1, n+1)]
    end = 0; col = 0; row = 0
    while (n > 0):
        answer, end = rotate(answer, end+1, row, col, n)
        col += 1; row += 2; n -= 3
    return list(reduce(lambda x, y: x+y, answer))

def rotate(answer, start, row, col, n):
    for i in range(start, start+n):
        answer[row][col] = i
        row += 1
    row -= 1
    
    for i in range(start+n, start+(2*n)-1):
        col += 1
        answer[row][col] = i
        
    for i in range(start+(2*n)-1, start+(3*n)-3):
        row -= 1
        col -= 1
        answer[row][col] = i
        
    return answer, start+(3*n)-4
        