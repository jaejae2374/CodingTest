from collections import deque

def solution(maps):
    d = {}; answer = 0; cnt = 0;
    for row in range(len(maps)):
        for col in range(len(maps[0])):
            if maps[row][col] not in ["O", "X"]:
                d[maps[row][col]] = (row, col)
                cnt += 1
            if cnt == 3: break
    sl = get_short(d["S"], d["L"], maps)
    if sl == -1: return -1
    le = get_short(d["L"], d["E"], maps)
    if le == -1: return -1 
    return sl+le

def get_short(start, end, maps):
    d = {f"{start[0]},{start[1]}": 0}
    bfs = deque()
    bfs.append(start)
    rows = len(maps); cols = len(maps[0])
    while bfs:
        row, col = bfs.popleft()
        t = d[f"{row},{col}"]
        if row-1>=0 and maps[row-1][col] != "X":
            if d.get(f"{row-1},{col}"):
                if d[f"{row-1},{col}"] > t+1:
                    d[f"{row-1},{col}"] = t+1
                    bfs.append((row-1, col))
            else:
                d[f"{row-1},{col}"] = t+1
                bfs.append((row-1, col))
        if row+1<rows and maps[row+1][col] != "X":
            if d.get(f"{row+1},{col}"):
                if d[f"{row+1},{col}"] > t+1:
                    d[f"{row+1},{col}"] = t+1
                    bfs.append((row+1, col))
            else:
                d[f"{row+1},{col}"] = t+1
                bfs.append((row+1, col))
        if col-1>=0 and maps[row][col-1] != "X":
            if d.get(f"{row},{col-1}"):
                if d[f"{row},{col-1}"] > t+1:
                    d[f"{row},{col-1}"] = t+1
                    bfs.append((row, col-1))
            else:
                d[f"{row},{col-1}"] = t+1
                bfs.append((row, col-1))
        if col+1<cols and maps[row][col+1] != "X":
            if d.get(f"{row},{col+1}"):
                if d[f"{row},{col+1}"] > t+1:
                    d[f"{row},{col+1}"] = t+1
                    bfs.append((row, col+1))
            else:
                d[f"{row},{col+1}"] = t+1
                bfs.append((row, col+1))
    if d.get(f"{end[0]},{end[1]}"):
        return d[f"{end[0]},{end[1]}"]
    else:
        return -1
    