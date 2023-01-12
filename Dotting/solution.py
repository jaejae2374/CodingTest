from math import sqrt
def solution(k, d):
    answer = 0
    m = d-d%k
    for i in range(m, -1, -k):
        answer+=int(sqrt(d**2 - i**2))//k + 1
    return answer
