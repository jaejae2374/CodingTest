import copy
def solution(maps):
    if maps[-1][-2] == 0 and maps[-2][-1] == 0:
        return -1
    maps[0][0] = 0
    return move(maps, 0, 0)

def move(maps, row, col):
    if row == len(maps) - 1 and col == len(maps[0]) - 1: 
        return 1
    n_list = []
    if row+1 < len(maps) and maps[row+1][col] == 1:
        maps_ = copy.deepcopy(maps)
        maps_[row+1][col] = 0
        n = move(maps_, row+1, col)
        if n > 0:
            n_list.append(n)
    if col+1 < len(maps[0]) and maps[row][col+1] == 1:
        maps_ = copy.deepcopy(maps)
        maps_[row][col+1] = 0
        n = move(maps_, row, col+1)
        if n > 0:
            n_list.append(n)
    if row-1 > 0 and maps[row-1][col] == 1:
        maps_ = copy.deepcopy(maps)
        maps_[row-1][col] = 0
        n = move(maps_, row-1, col)
        if n > 0:
            n_list.append(n)
    if col-1 > 0 and maps[row][col-1] == 1:
        maps_ = copy.deepcopy(maps)
        maps_[row][col-1] = 0
        n = move(maps_, row, col-1)
        if n > 0:
            n_list.append(n)
    if len(n_list) == 0:
        return -1
    else:
        return min(n_list) + 1
        