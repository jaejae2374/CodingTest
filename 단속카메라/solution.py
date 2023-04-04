def solution(routes):
    routes.sort(key=lambda x: x[0])
    answer = 1
    std = 30000
    for start, end in routes:
        if start > std:
            answer += 1
            std = end
        std = min(std, end)
    return answer
