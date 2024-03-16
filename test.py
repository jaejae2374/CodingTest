from collections import defaultdict, deque
from math import inf
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = inf
    def check(x, y, idx):
        if (x==rectangle[idx][0] and rectangle[idx][1]<=y<=rectangle[idx][3]) or (x==rectangle[idx][2] and rectangle[idx][1]<=y<=rectangle[idx][3]):
            return True
        if (y==rectangle[idx][1] and rectangle[idx][0]<=x<=rectangle[idx][2]) or (y==rectangle[idx][3] and rectangle[idx][0]<=x<=rectangle[idx][2]):
            return True
        else:
            return False
        
    start = None; dr = None;
    dx = defaultdict(lambda: -1); dy = defaultdict(lambda: -1)
    for rec, xy in enumerate(rectangle):
        x1, y1, x2, y2 = xy
        if (characterX==x1 and y1<=characterY<=y2) or (characterX==x2 and y1<=characterY<=y2):
            start = rec; dr = "v"
        if (characterY==y1 and x1<=characterX<=x2) or (characterY==y2 and x1<=characterX<=x2):
            start = rec; dr = "h"
        dx[x1]=rec; dx[x2]=rec; dy[y1]=rec; dy[y2]=rec
    
    dfs = deque()
    if dr=="h":
        dfs.append([characterX, characterY, start, 0, "l"])
        dfs.append([characterX, characterY, start, 0, "r"])
    else:
        dfs.append([characterX, characterY, start, 0, "u"])
        dfs.append([characterX, characterY, start, 0, "d"])
    while dfs:
        cx, cy, idx, dt, dr = dfs.popleft()
        if cx==itemX and cy==itemY:
            answer = min(answer, dt)
            continue
        if dr=="l":
            nx, ny = cx-1, cy
            if check(nx, ny, idx):
                if dx[nx]!=idx and dx[nx]>-1:
                    if check(nx, ny+1, idx):
                        dfs.appendleft([nx, ny, dx[nx], dt+1, "d"])
                    else:
                        dfs.appendleft([nx, ny, dx[nx], dt+1, "u"])
                else:
                    dfs.appendleft([nx, ny, idx, dt+1, dr])
            else:
                if check(cx, cy+1, idx):
                    dfs.appendleft([cx, cy+1, idx, dt+1, "u"])
                else:
                    dfs.appendleft([cx, cy-1, idx, dt+1, "d"])
        elif dr=="r":
            nx, ny = cx+1, cy
            if check(nx, ny, idx):
                if dx[nx]!=idx and dx[nx]>-1:
                    if check(nx, ny+1, idx):
                        dfs.appendleft([nx, ny, dx[nx], dt+1, "d"])
                    else:
                        dfs.appendleft([nx, ny, dx[nx], dt+1, "u"])
                else:
                    dfs.appendleft([nx, ny, idx, dt+1, dr])
            else:
                if check(cx, cy+1, idx):
                    dfs.appendleft([cx, cy+1, idx, dt+1, "u"])
                else:
                    dfs.appendleft([cx, cy-1, idx, dt+1, "d"])
        elif dr=="u":
            nx, ny = cx, cy+1
            if check(nx, ny, idx):
                if dy[ny]!=idx and dy[ny]>-1:
                    if check(nx+1, ny, idx):
                        dfs.appendleft([nx, ny, dy[ny], dt+1, "l"])
                    else:
                        dfs.appendleft([nx, ny, dy[ny], dt+1, "r"])
                else:
                    dfs.appendleft([nx, ny, idx, dt+1, dr])
            else:
                if check(cx+1, cy, idx):
                    dfs.appendleft([cx+1, cy, idx, dt+1, "r"])
                else:
                    dfs.appendleft([cx-1, cy, idx, dt+1, "l"])
        else:
            nx, ny = cx, cy-1
            if check(nx, ny, idx):
                if dy[ny]!=idx and dy[ny]>-1:
                    if check(nx+1, ny, idx):
                        dfs.appendleft([nx, ny, dy[ny], dt+1, "l"])
                    else:
                        dfs.appendleft([nx, ny, dy[ny], dt+1, "r"])
                else:
                    dfs.appendleft([nx, ny, idx, dt+1, dr])
            else:
                if check(cx+1, cy, idx):
                    dfs.appendleft([cx+1, cy, idx, dt+1, "r"])
                else:
                    dfs.appendleft([cx-1, cy, idx, dt+1, "l"])
        print(dfs)
    return answer

print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8))