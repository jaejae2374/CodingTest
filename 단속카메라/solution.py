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

print([[-20,-15], [-14,-5], [-18,-13], [-5,-3]])