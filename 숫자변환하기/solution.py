from collections import deque
def solution(x, y, n):
    if x == y: return 0
    bfs = deque()
    bfs.append(x)
    d = {x: 0}
    while bfs:
        num = bfs.popleft()
        case1 = num*3
        case2 = num*2
        case3 = num+n
        if case1 <= y:
            if d.get(case1):
                if d[case1] > d[num] + 1:
                    d[case1] = d[num] + 1
                    bfs.append(case1)
            else:
                d[case1] = d[num] + 1
                bfs.append(case1)
        if case2 <= y:
            if d.get(case2):
                if d[case2] > d[num] + 1:
                    d[case2] = d[num] + 1
                    bfs.append(case2)
            else:
                d[case2] = d[num] + 1
                bfs.append(case2)
        if case3 <= y:
            if d.get(case3):
                if d[case3] > d[num] + 1:
                    d[case3] = d[num] + 1
                    bfs.append(case3)
            else:
                d[case3] = d[num] + 1
                bfs.append(case3)
    answer = d[y] if d.get(y) else -1
    return answer
