def solution(maps):
    if len(maps) >= 2 and len(maps[0]) >= 2:
        if maps[-1][-2] == 0 and maps[-2][-1] == 0:
            return -1
    
    bfs = [(0, 0)]
    while bfs:
        row, col = bfs.pop(0)
        d = maps[row][col]
        if row+1 < len(maps):
            if maps[row+1][col] == 1 or maps[row+1][col] > d+1:
                maps[row+1][col] = d+1
                bfs.append((row+1, col))
        if col+1 < len(maps[0]):
            if maps[row][col+1] == 1 or maps[row][col+1] > d+1:
                maps[row][col+1] = d+1
                bfs.append((row, col+1))
        if row-1 >= 0:
            if maps[row-1][col] == 1 or maps[row-1][col] > d+1:
                maps[row-1][col] = d+1
                bfs.append((row-1, col))
        if col-1 >= 0:
            if maps[row][col-1] == 1 or maps[row][col-1] > d+1:
                maps[row][col-1] = d+1
                bfs.append((row, col-1))
    if maps[-1][-1] == 1:
        return -1
    else:
        return maps[-1][-1]
