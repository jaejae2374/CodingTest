def solution(e, starts):
    div = [1]*(e+1)
    answer = [0]*(e+1)
    i = 2
    for i in range(2,e+1):
        for j in range(i*2,e+1,i):
            div[j] += 1
    answer[e] = e
    for i in range(e-1, 0, -1):
        if div[i] >= div[answer[i+1]]:
            answer[i] = i
        else:
            answer[i] = answer[i+1]
    return [answer[s] for s in starts]
