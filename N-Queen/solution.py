def solution(n):
    answer = 0
    pan = [[0]*n for i in range(n)]
    for i in range(n):
        pan[i][0] = 1
        answer += choose(pan, 1, n)
        pan[i][0] = 0
    return answer

def choose(pan, idx, n):
    cnt = 0
    if idx == n:
        return 1
    for i in range(n):
        if sum(pan[i]) == 0:
            isOk = True
            tmp = min(i, idx)
            for j in range(tmp):
                if pan[i-j-1][idx-j-1] == 1:
                    isOk = False
                    break
            tmp = min(n-i-1, idx)
            for j in range(tmp):
                if pan[i+j+1][idx-j-1] == 1:
                    isOk=False
                    break
            if isOk:
                pan[i][idx] = 1
                cnt += choose(pan, idx+1, n)
                pan[i][idx] = 0
    return cnt

