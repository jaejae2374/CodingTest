def move(d, pos):
    if d == 'U':
        if pos[1] + 1 < 6:
            pos[1] += 1
    elif d == 'D':
        if pos[1] - 1 > -6:
            pos[1] -= 1
    elif d == 'R':
        if pos[0] + 1 < 6:
            pos[0] += 1
    else:
        if pos[0] - 1 > -6:
            pos[0] -= 1
    return pos

def solution(dirs):
    visited = {}
    pos = [0, 0]
    answer = 0
    for d in dirs:
        start = ''.join(map(lambda x: str(x), pos))
        pos = move(d, pos)
        end = ''.join(map(lambda x: str(x), pos))
        if start == end:
            continue
        path_1 = start + end
        path_2 = end+start
        if not (visited.get(path_1, False) or visited.get(path_2, False)):
            visited[path_1] = True
            visited[path_2] = True
            answer += 1
    return answer
