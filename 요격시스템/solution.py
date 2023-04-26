def solution(targets):
    answer = 1
    targets.sort(key=lambda x: x[0])
    std=(10**8)+1
    for s, e in targets:
        if s>=std:
            answer+=1
            std=e
        std=min(std, e)
        
    return answer
