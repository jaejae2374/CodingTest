def solution(left, right):
    cnts = [0]*1001
    for i in range(1, 1001):
        for j in range(1, 1000//i + 1):
            cnts[i*j] += 1
    answer = 0
    for n in range(left, right+1):
        if cnts[n] % 2 == 0:
            answer += n
        else:
            answer -= n
    return answer
