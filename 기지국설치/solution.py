def install(n, l):
    d, m = divmod(n, l)
    return d+1 if m!=0 else d

def solution(n, stations, w):
    answer = 0
    l = w*2+1
    std = 1
    for s in stations:
        answer+=install(s-w-std, l)
        std=s+w+1
    if std>n:
        return answer
    else:
        answer+=install(n-std+1, l)
    return answer
