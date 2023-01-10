import copy

def solution(n):
    answer = 0
    for i in range(n):
        pan = [[0]*n for i in range(n)]
        pan[i][0] = 1
        answer += choose(pan, 1, n)
    return answer

def choose(pan, start, n):
    cnt = 0
    if start == n:
        return 1
    for i in range(n):
        if sum(pan[i]) == 0:
            isOk = True
            tmp = min(i, start)
            for j in range(tmp):
                if pan[i-j-1][start-j-1] == 1:
                    isOk = False
                    break
            tmp = min(n-i-1, start)
            for j in range(tmp):
                if pan[i+j+1][start-j-1] == 1:
                    isOk=False
                    break
            if isOk:
                pan_ = copy.deepcopy(pan)
                pan_[i][start] = 1
                cnt += choose(pan_, start+1, n)
    return cnt
