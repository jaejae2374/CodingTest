def solution(a, b, n):
    answer = 0
    tmp = 0
    isFinished = False
    while True:
        d, m = divmod(n, a)
        tmp += m
        if d > 0:
            answer += d*b
            n = d*b
            isFinished = False
        else:
            n = tmp
            if isFinished: break
            tmp = 0
            isFinished = True
    return answer
