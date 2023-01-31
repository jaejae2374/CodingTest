def solution(m, n, board):
    board_ = list(map(lambda x: list(x)[::-1], zip(*board)))
    answer, before = 0, 0
    while True:
        d = {}
        for i in range(1, n):
            for j in range(1, m):
                s = set([board_[i][j], board_[i-1][j], board_[i][j-1], board_[i-1][j-1]])
                if len(s) == 1 and s != {"0"}:
                    if not d.get(f"{i},{j}"):
                        answer+=1
                        d[f"{i},{j}"]=True
                    if not d.get(f"{i-1},{j}"):
                        answer+=1
                        d[f"{i-1},{j}"]=True
                    if not d.get(f"{i},{j-1}"):
                        answer+=1
                        d[f"{i},{j-1}"]=True
                    if not d.get(f"{i-1},{j-1}"):
                        answer+=1
                        d[f"{i-1},{j-1}"]=True
        if answer == before:
            break
        for k in d:
            i, j = map(lambda x: int(x), k.split(","))
            board_[i][j] = "_"
        for b in board_:
            while "_" in b:
                b.remove("_")
                b.append("0")
        before = answer
    return answer
