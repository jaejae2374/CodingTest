from math import factorial

def solution(n, k):
    l = [i for i in range(1, n+1)]
    answer = []
    total = 0
    while len(l) > 1:
        for i in l:
            total += factorial(len(l)-1)
            if total >= k:
                answer.append(i)
                total -= factorial(len(l)-1)
                l.remove(i)
                break
    return answer + l
